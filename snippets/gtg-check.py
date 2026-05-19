from sqlmodel import Session, select

from relevant.models.enums import StoryLifecycle
from relevant.models.story import Story, StoryDep


# GTG = "green to go": a story can enter the pipeline only when a human has approved it
# and every dependency story it points to has already been closed.
def is_story_gtg(story_id: str, session: Session) -> bool:
    story = session.get(Story, story_id)
    if story is None or story.lifecycle != StoryLifecycle.APPROVED:
        return False  # not human-approved yet

    deps = session.exec(select(StoryDep).where(StoryDep.story_id == story_id)).all()
    for dep in deps:
        parent = session.get(Story, dep.depends_on_id)
        if parent is None or parent.lifecycle != StoryLifecycle.CLOSED:
            return False  # still blocked by unfinished upstream work

    return True


def evaluate_gtg(session: Session) -> list[tuple[str, str, str]]:
    candidates = session.exec(
        select(Story).where(Story.lifecycle == StoryLifecycle.APPROVED, Story.gtg == False)  # noqa: E712
    ).all()

    newly_gtg = []
    for story in candidates:
        if is_story_gtg(story.id, session):
            story.gtg = True                 # internal flag: safe to auto-start
            session.add(story)
            newly_gtg.append((story.id, story.title, story.epic_id))

    if newly_gtg:
        session.commit()
    return newly_gtg
