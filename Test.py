
class Test:
    def __init__(self, graph, from_station_id, to_station_id, algo, KPI):
        self.algo = algo
        self.graph = graph
        self.to_station = to_station_id
        self.from_station = from_station_id
        self.KPI = KPI

    def test(self):
        return self.KPI(self.graph, self.algo, self.from_station, self.to_station)
