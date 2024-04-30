import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_line_plot():
    # Read data and clean it
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df_cleaned = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_cleaned.index, df_cleaned['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.close()


def draw_bar_plot():
    # Read data and clean it
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df_cleaned = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Group data by year and month, calculate average page views
    df_monthly = df_cleaned.groupby([df_cleaned.index.year, df_cleaned.index.month]).mean().unstack()
    df_monthly.index.name = 'Year'
    df_monthly.columns = df_monthly.columns.get_level_values(1)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_monthly.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views by Month (Years 2016-2019)')
    ax.legend(title='Months')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.close()


def draw_box_plot():
    # Read data and clean it
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df_cleaned = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Prepare data for box plots
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.close()
