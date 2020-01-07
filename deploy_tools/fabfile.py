import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/glowingEdge/TDD-with-Python.git'
SITE_URL = 'staging.tdd-python.cf'
def deploy():
    server_aws()
    site_folder = f'/home/{env.user}/sites/{SITE_URL}'  
    run(f'mkdir -p {site_folder}')  
    with cd(site_folder):  
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')

def _update_virtualenv():
    if not exists('tddenv/bin/pip'):
        run(f'python3.6 -m venv tddenv')
    run('./tddenv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_static_files():
    run('./tddenv/bin/python manage.py collectstatic --noinput')

def _update_database():
    run('./tddenv/bin/python manage.py migrate --noinput')

def server_aws():
    env.hosts = ['INPUT_EC2INFO.amazonaws.com']
    env.user = 'elspeth'
    env.key_filename = 'C:/source/tdd-python.pem'
