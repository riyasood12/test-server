import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import io

    return io, mo, pd


@app.cell
def _(mo):
    mo.md("""
    # Interactive CSV Data Explorer
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **Please upload a CSV file using the below button**
    """)
    return


@app.cell
def _(mo):
    file_upload = mo.ui.file(label = "Upload a CSV file")
    file_upload
    return (file_upload,)


@app.cell
def _(file_upload, io, mo, pd):
    df = None
    if not file_upload.value:
        mo.md("**Please upload a CSV file to begin**")
        df = pd.DataFrame()
    else:
        file_contents_bytes = file_upload.value[0].contents
        csv_file_object = io.BytesIO(file_contents_bytes)
        df = pd.read_csv(csv_file_object)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, mo):
    ui = None
    expression = None
    category = None
    if df is not None and not df.empty:
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        categorical_cols = df.select_dtypes(exclude="number").columns.tolist()
        expression = mo.ui.dropdown(numeric_cols, label="Expression", value='expression')
        category = mo.ui.dropdown(categorical_cols, label="Category", value='condition')
        ui = mo.vstack([expression, category])
    return category, expression, ui


@app.cell
def _(df, mo):
    text_ui = None
    if df is not None and not df.empty:
        text_ui = mo.md("""**Calculating grouped average based on the selected gene and condition.**""")
    text_ui
    return


@app.cell
def _(ui):
    ui
    return


@app.cell
def _(category, df, expression):
    selected_df = None
    if df is not None and not df.empty and expression.value is not None and category.value is not None:
        selected_df = df[[expression.value, category.value]]
    return (selected_df,)


@app.cell
def _(category, selected_df):
    avg_df = None
    if selected_df is not None:
        avg_df = selected_df.groupby(category.value).mean().rename(columns={'expression' : f"Average expression after grouping {category.value}"})
    return (avg_df,)


@app.cell
def _(avg_df):
    avg_df
    return


if __name__ == "__main__":
    app.run()
