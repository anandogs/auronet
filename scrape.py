''' program to scrape all the happenings in Auroville from Auronet '''
import csv

def main():
    ''' main function '''

    import requests
    from bs4 import BeautifulSoup

    result = requests.get("https://auroville.org.in/")
    src = result.content
    soup = BeautifulSoup(src, features="html.parser")

    rows = soup.find_all('tr')

    date_range = []
    activity_range = []
    link_range = []
    timings_range = []

    for row in rows:
        activities = row.find_all('div', {'class':"view-field view-data-node-title node-title"})
        timings = row.find_all('div', {'class':'view-field view-data-node-data-field-event-date-field-event-date-value node-data-field-event-date-field-event-date-value'})
        dates = row.find_all('div', {'class':'event_date_header_date'})

        for i in range(len(activities)):
            for date in dates:
                date_range.append(date.text)

        for activity in activities:
            activity_range.append(activity.text)
            data_link = activity.find('a')
            link_range.append(data_link['href'])

        for time in timings:
            timings_range.append(time.text)

    data_to_print = [date_range, timings_range, activity_range, link_range]
    arranged_data = zip(*data_to_print)

    with open('activities.csv', 'w', newline='') as file:
        thewriter = csv.writer(file)
        thewriter.writerow(['Date', 'Timing', 'Activity', 'Link'])
        for data in arranged_data:
            thewriter.writerow(data)

if __name__ == '__main__':
    main()
