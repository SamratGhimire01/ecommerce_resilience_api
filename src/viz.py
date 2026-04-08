from analysis import data, get_content_type_distribution, get_top_countries, get_yearly_trend, get_rating_distribution, get_duration_stats
import matplotlib.pyplot as plt


def plot_content_distribution(data):
    results = get_content_type_distribution(data)
    plt.bar(results.keys(), results.values())
    plt.title("Content Type Distribution")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()
    
def plot_yearly_trend(data):
    results = get_yearly_trend(data)
    plt.plot(results.keys(),results.values())
    plt.title("Yearly Trends")
    plt.xlabel("Years")
    plt.ylabel("Movies Counts")
    plt.show()
    
    
def plot_top_countries(data):
    results = get_top_countries(data)
    plt.bar(results.keys(),results.values())
    plt.title("Total Movies and TV Shows Count according to the Countries.")
    plt.xlabel("Country")
    plt.ylabel("Total Movies")
    plt.show()

def plot_rating_distribution(data):
    results = get_rating_distribution(data)
    plt.bar(results.keys(),results.values())
    plt.title("Rating Distrubution")
    plt.xlabel("Rating")
    plt.ylabel("Total Movies according to rating.")
    plt.show()

def plot_average_duration(data):
    results = get_duration_stats(data)
    plt.bar(results.keys(),results.values())
    plt.title("Average Duration of Movies and Average Seasons.")
    plt.xlabel("Names")
    plt.ylabel("Average")
    plt.show()


plot_average_duration(data)
