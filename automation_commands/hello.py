import click

@click.command()
@click.option('--count', default=1, help="count of hello")
@click.option('-m', '--message', help="takes message from user")
@click.option('-V', '--version',  is_flag=True, help="show module version")
def salamla(count, message, version):
    if version:

        click.echo('Salamla: 1.0.0')
        return
    if not message:
        message = 'salam'
    for i in range(count):
        click.echo(message)
    


if __name__ == '__main__':
    salamla()