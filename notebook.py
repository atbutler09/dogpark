import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import plotly
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is a test sentence! :)
    """)
    return


if __name__ == "__main__":
    app.run()
