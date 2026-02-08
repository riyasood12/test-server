import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Hello Riya, this is the marimo application
    """)
    return


if __name__ == "__main__":
    app.run()
