from csv import DictReader, DictWriter
import random
from ascii_magic import from_image
import shutil
import sys
from rich.prompt import Prompt
from rich.console import Console
from tabulate import tabulate



def main():
    choice = show_intro()
    if choice == "1":
        main_game()
    elif choice == "2":
        show_scores()
        return_menu()
    elif choice == "3":
        show_rules()
        return_menu()
    elif choice == "4":
        clear_score()
        return_menu()
    elif choice == "5":
        Console().print("[bold red]Goodbye![/]")
        sys.exit()


def main_game():            # main_game function
    category, difficulty = take_input()
    levels = gen_guesses(category, difficulty)
    scores = 0
    for level in levels:
        scores += simulate(level["name"], level["hint"])
    Console().print(f"\n[bold cyan]{score_msg(scores, difficulty)}[/]")
    save_score(category, difficulty, scores)

    
def simulate(name, hint):           # simulate the whole game
    scores = 0
    fails = 0
    gen_images(name)
    Console().print(f"\n[bold blue]Hint: {hint.title()}.[/]")
    while True:
        ans = Prompt.ask("[bold white]Guess the Image[/]").lower().strip()

        if ans == name:
            scores += 1
            break
        if ans == "quit":
            Console().print("\n[cyan]Thanks for playing![/] [bold red]Goodbye[/] 👋")
            sys.exit()
        elif ans != name:
            fails += 1
            Console().print(f"[bold red]Wrong![/] Try again. [bold white]{5 - fails}[/] guesses remaining")
            if fails == 5:
                fails -= 5
                Console().print(f"\n[bold white]The answer is {name.title()}[/]")
                break

    return scores

def clear_score():      #clears scores
    while True:
        confirm = Prompt().ask("\n[red]Are you sure you want to clear all score history? (yes/no)[/]").strip().lower()
        if confirm == "yes":
            difficulties = ["easy", "medium", "hard"]
            for difficulty in difficulties:
                with open(f"scores/{difficulty}_scores.csv", "w", newline="") as f:
                    writer = DictWriter(f, ["category","scores"])
                    writer.writeheader()
            Console().print("[bold red]Score Cleared[/]")
            break
        elif confirm == "no":
            Console().print("[bold yellow]Canceled. No scores were cleared.[/]")
            break
        else:
            Console().print("[bold red]Invalid input. Please type 'Yes' or 'No'.[/]")


def return_menu(): #return to the main menu
    while True:
        again = Prompt.ask("\nDo you want to return to the main menu? [cyan][Yes/No][/]").lower().strip()
        if again == "no":
            Console().print("\n[bold red]Goodbye[/] 👋")
            sys.exit()
        elif again == "yes":
            main()
            break
        else:
            Console().print("[bold red]Invalid input. Please type 'Yes' or 'No'.[/]")

# takes n names from csv
def gen_images(name):
    columns, _ = shutil.get_terminal_size()
    ascii_columns = int(columns * 0.95)

    img = from_image(rf"stock_images\{name}.png")
    img.to_terminal(columns=ascii_columns)



def take_input():   # ask game category and difficulty
    avail_category = {"1": "attack on titan", "2": "berserk", "3": "one piece", "4": "demon slayer", "5": "naruto"}
    diffs = ["easy", "medium", "hard"]
    while True:
        category = Prompt.ask(
"""
\n[bold cyan]==============================[/]
[bold green]     Available Categories     [/]
[bold cyan]==============================[/]
[yellow][1][/] [white]Attack on Titan[/]
[yellow][2][/] [white]Berserk[/]
[yellow][3][/] [white]One Piece[/]
[yellow][4][/] [white]Demon Slayer[/]
[yellow][5][/] [white]Naruto[/]
\n[bold white]Select a category[/]""", choices=["1", "2", "3", "4", "5"])
        if category in avail_category.keys():
            pass
            while True:
                diff = Prompt.ask("Choose difficulty [bold cyan][Easy/Medium/Hard][/] ").strip().lower()
                if diff in diffs:
                    return avail_category[category], diff



def gen_guesses(category, diff):    # generate name and hints
    with open(
        f"category/{category}/{diff} {category}.csv",
    ) as file:
        rows = list(DictReader(file))
    random_rows = random.sample(rows, 5)
    return random_rows



def score_msg(s, d):        # return score msg

    if d == "easy":
        excellent = [
            "5 out of 5! Perfect score! are you psychic or what? 🔮",
            "Full marks! Absolute domination. 👑",
            "Flawless run! textbook performance. 💯",
        ]
        good = [
            f"{s} out of 5! solid skills, you are close to greatness! ⚡",
            f"{s} out of 5! Not bad! Just a couple of misses. You are nearly there! 🚀",
            f"{s} out of 5! Good job! a few stumbles but overall impressive! 🎯",
        ]
        low = [
            f"{s} out of 5... at least you turned up! 😂",
            f"{s} out of 5! Oops... did you type randomly? Time for a comeback! 🫣",
            f"{s}/5! Rough round! let’s pretend it never happened. 👀",
        ]

        if s == 5:
            return random.choice(excellent)
        elif 3 <= s <= 4:
            return random.choice(good)
        else:
            return random.choice(low)

    elif d == "medium":
        excellent = [
            f"{s} out of 10! Expert level unlocked. 🌟",
            "Crushed it! That is how pros do it. 🔥",
            "On point! you made this look easy. 🏆",
        ]
        good = [
            f"{s} out of 10. Pretty good! Some tough ones in there, right? 😉",
            f"{s} out of 10! Respectable score! You are definitely no rookie. 👌",
            f"{s} out of 10. Decent run! With a little sharpening you will ace it. ✨",
        ]
        low = [
            f"{s} out of 10... did you blink too long? 😅",
            f"{s}/10! No worries, we all have off days. Rematch? 🫡",
            "That was… an attempt. Let’s give it another shot! 💀",
        ]

        if s >= 9:
            return random.choice(excellent)
        elif 5 <= s <= 8:
            return random.choice(good)
        else:
            return random.choice(low)

    elif d == "hard":
        excellent = [
            f"{s} out of 15! You just flexed on this game. 🚀",
            "Massive brain detected! you aced it! 🧠",
            "Legendary performance! pure dominance! 💥",
        ]
        good = [
            f"{s} out of 15! Good effort! You are on the right track. 💪",
            f"{s} out of 15! Not too shabby! Some tough ones but you held strong. 🎉",
            f"{s}/15. Somewhat impressive score! You are clearly above average. 🏅",
        ]
        low = [
            f"{s} out of 15... at least you made it entertaining! 😄",
            f"{s} out of 15... that was a creative guessing session! 😂",
            f"Well... {s}/15 points for trying. Want redemption? 😎",
        ]

        if s >= 14:
            return random.choice(excellent)
        elif 7 <= s <= 13:
            return random.choice(good)
        else:
            return random.choice(low)

def show_rules():    # print game rules
    Console().print(
"""
\n[bold cyan]=============== How to Play ===============[/bold cyan]
\n[green]1.[/] Choose a category.
[green]2.[/] Choose a difficulty.
[green]3.[/] You will be shown [bold]5 ASCII images[/bold], one by one.
[green]4.[/] For each image, you will get a hint and must guess the character's full name.
[green]5.[/] You have [bold red]5 chances[/] to guess each character.
[green]6.[/] Case doesn't matter (you can use lowercase or uppercase).
[green]7.[/] Guess correctly to win! The answer will be shown after your tries are over.
[green]8.[/] Type 'quit' anytime to exit the game early.
\n[bold magenta]Good luck. Have fun! 🎉[/bold magenta]
"""
)
    

def show_intro(): #show intro
    _ = Prompt.ask(
"""
\n[bold white]===================================[/]
[bold cyan]          Guess no Jutsu!           [/]
[bold white]===================================[/]\n
[bold green]What would you like to do?[/]
[blue][1][/blue] Play the Game 🎮
[blue][2][/blue] View Score History ⭐
[blue][3][/blue] How to Play 📜
[blue][4][/blue] Clear All Score Records 🗑️
[blue][5][/blue] Exit ❌ \n
[bold]Enter your choice[/]""", choices=["1", "2", "3", "4", "5"])   
    return _

def save_score(category,diff,score):   #saves game scores
    with open(f"scores/{diff}_scores.csv", "a", newline="") as f:
        writer = DictWriter(f, ["category","scores"])
        writer.writerow({"category": category, "scores": score})

def take_input_for_score_history():     #take inputs to show scores
    avail_category = {"1": "attack on titan", "2": "berserk", "3": "one piece", "4": "demon slayer", "5": "naruto"}
    diffs = ["easy", "medium", "hard"]
    while True:
        category = Prompt.ask(
"""
\n[bold cyan]==============================[/]
[bold magenta]     Score History Menu     [/]
[bold cyan]==============================[/]
[yellow][1][/] [white]Attack on Titan[/]
[yellow][2][/] [white]Berserk[/]
[yellow][3][/] [white]One Piece[/]
[yellow][4][/] [white]Demon Slayer[/]
[yellow][5][/] [white]Naruto[/]
\n[bold white]Select a category[/]""", choices=["1", "2", "3", "4", "5"])
        if category in avail_category.keys():
            pass
            while True:
                diff = Prompt.ask("Choose difficulty [bold cyan][Easy/Medium/Hard][/] ").strip().lower()
                if diff in diffs:
                    return avail_category[category], diff   


def show_scores():      #show scores
    category, diff = take_input_for_score_history()

    with open(f"scores/{diff}_scores.csv", "r") as file:
        reader = list(DictReader(file))
    try:
        headers = reader[0].keys()
    except IndexError:
        Console().print("[red]No history to show[/]")
        sys.exit()

    rows = []
    for row in reader:
        if row["category"] == category:
            rows.append(row.values())
    table = tabulate(rows, headers, tablefmt="fancy_grid") # type: ignore
    print(table)


if __name__ == "__main__":
    while True:
            main()
            while True:
                again = Prompt.ask("\nDo you want to play again? [bold cyan][Yes/No][/] ").lower().strip()
                if again == "no":
                    Console().print("\n[cyan]Thanks for playing![/] [bold red]Goodbye[/] 👋")
                    sys.exit()
                elif again == "yes":
                    break
                else:
                    Console().print("[bold red]Invalid input. Please type 'Yes' or 'No'.[/]")

