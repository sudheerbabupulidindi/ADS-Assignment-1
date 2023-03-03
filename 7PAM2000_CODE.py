import pandas as pd
import matplotlib.pyplot as plt

def plot_food_law_enforcement_returns(data_path):
    """
    Reads the local authority food law enforcement returns dataset from the given path
    and produces a line plot showing the total number of establishments, establishments 
    subject to formal enforcement actions, and the percentage of interventions achieved 
    by premises rated A-C, A, B, and C over the years 2003-2017.

    Parameters:
        data_path (str): The path to the dataset in CSV format.

    Returns:
        None.
    """

    # Read the dataset from the given path
    df = pd.read_csv(data_path, encoding='unicode_escape')

    # Select the relevant columns and rename them for clarity
    df = df[['Country', 'LA Name', 'Total number of establishments (including not yet rated and outside)(1)', 
             'Total number of establishments subject to formal enforcement action - Seizure, detention and surrender of food',
             'Total % of interventions achieved (premises rated A-C)', 'Total % of interventions achieved - premises rated A', 
             'Total % of interventions achieved - premises rated B', 'Total % of interventions achieved - premises rated C']]
    df.columns = ['Country', 'LA Name', 'Total establishments', 'Enforcement actions',
                  '% interventions achieved (A-C)', '% interventions achieved (A)',
                  '% interventions achieved (B)', '% interventions achieved (C)']

    # Group the data by LA Name and sum the values for each year
    df = df.groupby(['LA Name']).sum()

    # Transpose the data to have years as columns and percentages and counts as rows
    df = df.T

    # Set the plot size and style
    plt.figure(figsize=(12, 50))
    plt.style.use('seaborn-whitegrid')

    # Plot the data for each percentage and count
    for col in df.columns:
        plt.plot(df.index, df[col], label=col)

    # Add axis labels and legend
    plt.xlabel('Different Establishment over year 2003-2017')
    plt.ylabel('Count / Percentage')
    plt.title('Local Authority Food Law Enforcement Returns', fontsize=20)
    plt.legend(loc='best')

    # Display the plot
    plt.show()

plot_food_law_enforcement_returns(r'2019-20-enforcement-data-food-standards.csv')

def plot_interventions_by_la(data_path):
    """
    This function produces a stacked bar chart to show the percentage breakdown of interventions achieved for each local authority.

    Parameters:
    data_path (str): The file path for the food law enforcement dataset.

    Returns:
    None
    """
    # Read in the data and select the relevant columns
    df = pd.read_csv(data_path, encoding='unicode_escape')
    df = df[['LA Name', 'Total % of interventions achieved - premises rated A', 
             'Total % of interventions achieved - premises rated B', 'Total % of interventions achieved - premises rated C']]

    # Group the data by LA Name and sum the values for each category of intervention
    df_grouped = df.groupby(['LA Name']).sum()

    # Create a stacked bar chart
    fig, ax = plt.subplots(figsize=(40, 6))
    df_grouped.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel('Local Authority')
    ax.set_ylabel('Percentage of Premises')
    ax.set_title('Interventions Achieved by Local Authority', fontsize=30)
    ax.legend(loc='upper right')
    plt.show()

plot_interventions_by_la(r'2019-20-enforcement-data-food-standards.csv')

def plot_enforcement_vs_establishments(data_path):
    """
    This function produces a scatter plot to show the relationship between the number of establishments subject to formal enforcement action and the number of enforcement actions taken.

    Parameters:
    data_path (str): The file path for the food law enforcement dataset.

    Returns:
    None
    """
    # Read in the data and select the relevant columns
    df = pd.read_csv(data_path, encoding='unicode_escape')
    df = df[['LA Name', 'Total number of establishments subject to formal enforcement action - Seizure, detention and surrender of food',
             'Total number of establishments subject to formal enforcement actions - Simple cautions',
             'Total number of establishments subject to formal enforcement actions - Improvement notices',
             'Total number of establishments subject to Written warnings',
             'Total number of establishments subject to formal enforcement action - Prosecutions concluded']]

    # Group the data by LA Name and sum the values for each category of enforcement action
    df_grouped = df.groupby(['LA Name']).sum()

    # Create a scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df_grouped['Total number of establishments subject to formal enforcement action - Seizure, detention and surrender of food'], 
               df_grouped['Total number of establishments subject to formal enforcement actions - Simple cautions'] +
               df_grouped['Total number of establishments subject to formal enforcement actions - Improvement notices'] +
               df_grouped['Total number of establishments subject to Written warnings'] +
               df_grouped['Total number of establishments subject to formal enforcement action - Prosecutions concluded'])
    ax.set_xlabel('Number of Establishments Subject to Formal Enforcement Action')
    ax.set_ylabel('Number of Enforcement Actions Taken')
    plt.title('Number of Enforcement', fontsize=20)

plot_enforcement_vs_establishments(r'2019-20-enforcement-data-food-standards.csv')

