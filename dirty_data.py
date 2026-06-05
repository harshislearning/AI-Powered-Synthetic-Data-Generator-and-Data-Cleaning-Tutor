import random
import numpy as np
import pandas as pd


def add_missing_values(df, probability=0.1):

    for col in df.columns:

        df.loc[
            df.sample(frac=probability).index,
            col
        ] = np.nan

    return df


def add_duplicates(df, probability=0.1):

    duplicate_rows = df.sample(frac=probability)

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    return df


def add_typo(value):

    if isinstance(value, str) and len(value) > 3:

        idx = random.randint(
            0,
            len(value) - 1
        )

        value = (
            value[:idx]
            + random.choice(
                "abcdefghijklmnopqrstuvwxyz"
            )
            + value[idx + 1:]
        )

    return value


def add_typos(df, probability=0.1):

    for col in df.select_dtypes(
        include="object"
    ).columns:

        sampled = df.sample(
            frac=probability
        ).index

        df.loc[sampled, col] = (
            df.loc[sampled, col]
            .apply(add_typo)
        )

    return df


def add_case_issues(df, probability=0.1):

    for col in df.select_dtypes(
        include="object"
    ).columns:

        sampled = df.sample(
            frac=probability
        ).index

        df.loc[sampled, col] = (
            df.loc[sampled, col]
            .apply(
                lambda x:
                x.upper()
                if isinstance(x, str)
                else x
            )
        )

    return df


def add_extra_spaces(df, probability=0.1):

    for col in df.select_dtypes(
        include="object"
    ).columns:

        sampled = df.sample(
            frac=probability
        ).index

        df.loc[sampled, col] = (
            df.loc[sampled, col]
            .apply(
                lambda x:
                f" {x} "
                if isinstance(x, str)
                else x
            )
        )

    return df


def make_dataset_dirty(df, level):

    issues = []

    if level == "Easy":

        df = add_missing_values(df, 0.05)

        issues.append(
            "Missing Values"
        )

    elif level == "Medium":

        df = add_missing_values(df, 0.1)
        df = add_duplicates(df, 0.1)
        df = add_case_issues(df, 0.1)

        issues.extend([
            "Missing Values",
            "Duplicates",
            "Case Issues"
        ])

    elif level == "Hard":

        df = add_missing_values(df, 0.15)
        df = add_duplicates(df, 0.15)
        df = add_typos(df, 0.20)
        df = add_case_issues(df, 0.20)
        df = add_extra_spaces(df, 0.20)

        issues.extend([
            "Missing Values",
            "Duplicates",
            "Typos",
            "Case Issues",
            "Extra Spaces"
        ])

    return df, issues