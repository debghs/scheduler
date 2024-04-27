import click
from colorama import init, Fore, Style

# Initialize colorama
init()

@click.group()
def commands():
    pass 

@click.command()
@click.option('--name', prompt="enter name", help="the name of the user")
def hello(name):
    click.echo(f"Hello, {name}!")

PRIORITIES = {
    "o": ("optional", Fore.BLUE),
    "l": ("low", Fore.GREEN),
    "m": ("moderate", Fore.GREEN + Style.BRIGHT),
    "h": ("high", Fore.RED),
    "c": ("critical", Fore.RED + Style.BRIGHT)
}

END_COLOR = Style.RESET_ALL

@click.command()
@click.argument("priority",type=click.Choice(PRIORITIES.keys()),default="m")
@click.argument("taskfile",type=click.Path(exists=False),required=0)
@click.option("-n", "--name", prompt="enter task name", help="the name of task to be done")
@click.option("-d", "--desc", prompt="describe the task", help="the description of the task to be done")
def add_task(name, desc, priority, taskfile):
    filename = taskfile if taskfile is not None else "tasks.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc} [{PRIORITIES[priority][1]}{PRIORITIES[priority][0]}{END_COLOR}]\n")

@click.command()
@click.argument("idx",type=int,required=1)
def del_task(idx):
    with open("tasks.txt","r") as f:
        task_list = f.read().splitlines()
        task_list.pop(idx)
    with open("tasks.txt","w") as f:
        f.write("\n".join(task_list))
        f.write("\n")

@click.command()
@click.option("-p","--p",type=click.Choice(PRIORITIES.keys()))
@click.argument("task_file",type=click.Path(exists=True),required=0)
def task_list(p, task_file):
    filename = task_file if task_file is not None else "tasks.txt"
    with open(filename, "r") as f:
        task_list = f.read().splitlines()
        if p is None:
           for idx, task in enumerate(task_list):
                print(f"({idx}) - {task}") 
        else:
            for idx, task in enumerate(task_list):
                if f"{PRIORITIES[p][0]}" in task:
                    print(f"({idx}) - {PRIORITIES[p][1]}{task}{END_COLOR}")


commands.add_command(hello)
commands.add_command(add_task)
commands.add_command(del_task)
commands.add_command(task_list)

if __name__ == "__main__":
    commands()
