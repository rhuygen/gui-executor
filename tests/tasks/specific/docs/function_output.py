from pathlib import Path

from gui_executor.exec import exec_task, FileName, Directory

HERE = Path(__file__).parent.resolve()

@exec_task()
def print_bird_count(camera: str = "backyard", date: str = "today"):

    from rich.table import Table
    from rich.console import Console

    table = Table(title=f"Bird Count for {camera}")

    table.add_column("Date", justify="right", style="cyan", no_wrap=True)
    table.add_column("Bird name", style="magenta")
    table.add_column("Number", justify="center", style="green")

    for date, name, number in {
        ("16 Feb 2023", "ChiffChaff", 3),
        ("16 Feb 2023", "Robin", 1),
        ("16 Feb 2023", "Pigeon", 5),
        ("16 Feb 2023", "Magpie", 3),
        ("16 Feb 2023", "Sparrow", 10),
        ("16 Feb 2023", "Great tit", 9),
    }:
        table.add_row(date, name, str(number))

    console = Console(width=200)
    console.print(table)


@exec_task()
def preview_image(camera: str = "bird_house"):

    from IPython.display import Image, display

    image = Image(filename=HERE / f"{camera}.png")
    display(image)

    return image
