import typer
from rich.console import Console
import os
from dotenv import load_dotenv

# Loads the environment variables from the .env file
load_dotenv()

# Initializes Typer (for the CLI) and Rich (for beautiful terminal colors)
app = typer.Typer()
console = Console()

@app.command()
def scan(target_dir: str = typer.Argument(..., help="Path to the project directory to scan")):
    """
    Scans a directory for logic flaws using Claude Opus 4.7.
    """
    console.print("[bold green]Starting LogicLint...[/bold green]")
    console.print(f"Scanning target directory: [bold blue]{target_dir}[/bold blue]\n")
    
    # Checks if the API Key is configured
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "sua_chave_vai_aqui_quando_o_evento_comecar":
        console.print("[bold red]Error: ANTHROPIC_API_KEY not found or invalid in .env file.[/bold red]")
        raise typer.Exit(code=1)
        
    console.print("[bold green]✔ API Key found![/bold green] Ready to connect to Anthropic API.")
    console.print("[dim]Next step: Read files and send to Claude...[/dim]")

if __name__ == "__main__":
    app()