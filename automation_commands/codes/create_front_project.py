import click
import os


@click.command()
@click.option('-p', '--project', required=True, help='sdkjfds')
@click.option('--path', help='sdkjfds')
def create_project(project, path):
    html = None
    with open('index.html', 'r') as f:
        html = f.read()
    if path:
        os.chdir(path)
    os.mkdir(project)
    os.chdir(project)
    os.mkdir('css')
    os.mkdir('js')
    open('css/style.css', 'w').close()
    open('js/script.js', 'w').close()
    with open('index.html', 'w') as f:
        f.write(html)

    if click.confirm('git reponuz varmi? '):
        git_repo = click.prompt('repo unvani qeyd edin: ')
        os.system('git init')
        os.system(f'git remote add origin {git_repo}')
        os.system('git add .')
        os.system('git commit -m "project created"')
        os.system('git push origin master')
    


if __name__ == '__main__':
    create_project()