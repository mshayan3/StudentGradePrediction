import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create a directory to store visualizations if it doesn't exist
if not os.path.exists("Visualizations"):
    os.makedirs("Visualizations")

data = pd.read_csv('Cleaned/cleaned_a.csv')


def plot(data: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[['As_1', 'As_2', 'As_3', 'As_4']])
    plt.xlabel('Assessments')
    plt.ylabel('Scores')
    plt.title('Distribution of Scores across Assessments', wrap=True)
    plt.savefig('Visualizations/distribution_scores_across_assessments.png')  # Save the plot
    plt.show()


chart = plot(data)



def plot(data: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[['Qz_1', 'Qz_2', 'Qz_3', 'Qz_4']])
    plt.xlabel('Assessments')
    plt.ylabel('Scores')
    plt.title('Distribution of Scores across Quizzes', wrap=True)
    plt.savefig('Visualizations/distribution_scores_across_quizzes.png')  # Save the plot
    plt.show()


chart = plot(data)


def plot3(data: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.histplot(data, x="S_1", hue="Grade", multiple="stack", palette="husl")
    plt.suptitle('Histogram of S_1', wrap=True)
    plt.savefig('Visualizations/histogram_of_S_1.png')  # Save the plot
    plt.show()


chart = plot3(data)

data2 = pd.read_csv('Cleaned/cleaned_b.csv')


def plot4(data2: pd.DataFrame):
    sns.scatterplot(data=data2, x='S_1', y='S_2', hue='Grade')
    plt.title('Evaluate based on S_1 and S_2 and classify grade', wrap=True)
    plt.savefig('Visualizations/scatterplot_S_1_vs_S_2.png')  # Save the plot
    plt.show()


chart = plot4(data2)


def plot5(data2: pd.DataFrame):
    sns.displot(data=data2, x="As", hue="Grade", kde=True, palette="husl", multiple="stack")
    plt.title('Distribution of Assignment Grades', wrap=True)
    plt.gcf().set_size_inches(10, 10)  # Adjust width and height as needed
    plt.savefig('Visualizations/distribution_assignment_grades.png')  # Save the plot
    plt.show()

chart = plot5(data2)


def plot5_2(data2: pd.DataFrame):
    sns.displot(data=data2, x="Qz", hue="Grade", kde=True, palette="husl", multiple="stack")
    plt.title('Distribution of Quiz Grades', wrap=True)
    plt.gcf().set_size_inches(10, 10)  # Adjust width and height as needed
    plt.savefig('Visualizations/distribution_quiz_grades.png')  # Save the plot
    plt.show()

chart = plot5_2(data2)


def plot6(data2: pd.DataFrame):
    pass_count = data2[data2['Grade'] == 'Pass'].shape[0]
    fail_count = data2[data2['Grade'] == 'Fail'].shape[0]

    pass_percentage = (pass_count / (pass_count + fail_count)) * 100
    fail_percentage = (fail_count / (pass_count + fail_count)) * 100

    labels = ['Pass', 'Fail']
    sizes = [pass_percentage, fail_percentage]
    colors = ['#e6ffe6', '#ffcccc']  # using light colors
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=90)
    plt.axis('equal')
    plt.legend(title='Grade', loc='best')

    plt.title('What is the percentage of students who passed the course?', wrap=True)
    plt.savefig('Visualizations/pass_fail_percentage.png')  # Save the plot
    plt.show()


chart = plot6(data2)
