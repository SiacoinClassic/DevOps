import os
from git import Repo
from log_spinners import LogSpinners
from config import (
    NEBULOUSLABS_GIT_BASEURL,
    SIACOINCLASSIC_GIT_BASEURL,
    REPOSITORYS_DIR,
    DEPENDENCIES,
)


def update_repositorys():
    index = 1
    for repository in DEPENDENCIES:
        index_text = f'[{index}/{len(DEPENDENCIES)}]'
        log = LogSpinners(f'{index_text} {repository}: checking...')
        log.start()
        if os.path.exists(os.path.join(REPOSITORYS_DIR, repository)) is False:
            log.update(f'{index_text} {repository}: cloning...')
            repo = Repo.clone_from(
                f'{NEBULOUSLABS_GIT_BASEURL}{repository}.git',
                os.path.join(REPOSITORYS_DIR, repository),
                branch='master'
            )
            repo.create_remote(
                'github',
                url=f'{SIACOINCLASSIC_GIT_BASEURL}{repository}.git'
            )
            log.update(f'{index_text} {repository}: cloned!')
        else:
            log.update(f'{index_text} {repository}: pulling...')
            repo = Repo(os.path.join(REPOSITORYS_DIR, repository))
            repo.remotes.origin.pull()
            log.update(f'{index_text} {repository}: pulled!')
        log.update(f'{index_text} {repository}: pushing...')
        repo.remotes.github.push()
        log.update(f'{index_text} {repository}: pushed!')
        log.stop('success')
        index += 1


def main():
    update_repositorys()


if __name__ == '__main__':
    main()
