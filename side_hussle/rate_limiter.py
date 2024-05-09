from datetime import datetime
import json


class RateLimitedCalculator:

    """
    Note: Terminal or shell will be appropiate to test it.

    Approach to limit a method call for given uses limit within a minute.
    If limit reaches for current minute, it will throw an exception with message until
    the limit expires or starts a new minute.

    Let's test it:

    >>> obj = RateLimitedCalculator(5)
    >>> obj.getSum(4,5)
    9
    >>> obj.getSum(4,6)
    10
    >>> obj.getSum(4,7)
    11
    >>> obj.getSum(4,8)
    12
    >>> obj.getSum(4,9)
    13
    >>> obj.getSum(4,1)  # This line will throw error
    """

    def __init__(self, limit):
        self.limit = limit
        self.used = 0
        self.current_minute = datetime.now().minute

    def getSum(self, a, b):

        # Get current execution time
        execution_minute = datetime.now().minute

        # If execution itme & initialize base time is same
        if execution_minute == self.current_minute:

            # Check if limit is equal to used then throw error if it is
            if self.limit == self.used:
                raise Exception("Current minute limit reached!")

            # Else increase the used count
            self.used += 1
        else:

            # If current minute expires then assign new minute with used = 1
            self.current_minute = execution_minute
            self.used = 1

        return a + b


# Method two with offline functionality of keep tracking used & time


class RateLimitedCalculatorOffline:

    """
    Note: Terminal or shell will be appropiate to test it.

    It performs same task as above except it keeps track of the used execution &
    last initialized minute even if you terminate the program.

    Let's test it
    >>> obj = RateLimitedCalculatorOffline(5)
    >>> obj.getSum(4,5)
    9
    >>> obj.getSum(4,6)
    10
    >>> obj.getSum(4,7)
    11
    >>> obj.getSum(4,8)
    12
    >>> obj.getSum(4,9)
    13

    >>> obj.getSum(4,1) # This line will throw error
    """

    def __init__(self, limit=1):
        self.limit = limit
        self.data = self.get_or_load_data()

    def get_or_load_data(self):

        """
        Create or get time_tracker json file for tracking limit, minute and used count
        :return:
        dictionary object containing : last_tracked_time, limit & used

        """

        try:
            # If file found
            with open('../toph/time_tracker.json', 'r') as file:
                data = json.load(file)
                self.limit = self.limit
        except FileNotFoundError:
            # Else create a new one with given data
            data = {
                "last_tracked_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "limit": self.limit,
                "used": 0
            }
            with open('../toph/time_tracker.json', 'w') as file:
                json.dump(data, file, indent=4)
        return data

    def save_data(self):
        with open('../toph/time_tracker.json', 'w') as file:
            # Comment below line, and you'll get stuck with fixed limit value except deleting the json file :).
            self.data['limit'] = self.limit

            json.dump(self.data, file, indent=4)

    def getSum(self, a, b):

        # Get current execution time
        execution_minute = datetime.now()

        # Get last execution minute
        last_tracked_time = datetime.strptime(self.data['last_tracked_time'], '%Y-%m-%d %H:%M:%S')

        # If execution itme & initialize base time is same
        if execution_minute.minute == last_tracked_time.minute:

            # Check if limit is equal to used then throw error if it is
            if self.data["limit"] == self.data["used"]:
                raise Exception("Current minute limit reached!")

            # Else increase the used count
            self.data['used'] += 1

        else:

            # If current minute expires then assign new minute with used = 1
            self.data['last_tracked_time'] = execution_minute.strftime('%Y-%m-%d %H:%M:%S')
            self.data['used'] = 1

        self.save_data()

        return a + b


if __name__ == '__main__':
    """
    Testing procedure using doctest.
    """

    import doctest
    doctest.testmod()
