# ESPN-ff

This module prints the top 10 most scored points from
your ESPN fantasy football league


### Install

```bash
git clone https://github.com/billma12/espn-ff.git
```

### Usage

```bash
python main.py [leagueID]
```

### Preview

- <a href="https://ibb.co/hCLM2F"><img src="https://preview.ibb.co/fX2qwa/preview.png" alt="preview" border="0"></a>

### Notes
1. Make sure tabulate is installed

        pip install tabulate

2. Optional Features:

   1. Extend the results

          python main.py [leagueID] [top] [year]
        - e.g. if I want to view top 15 dating back to 2008 (default is 2011)

              python main.py 476859 15 2008
   2. Display league stats at any year

          python main.py 476859 stats 2015

        <a href="https://ibb.co/bxqFUv"><img src="https://preview.ibb.co/ncGB2F/Screen_Shot_2017_08_07_at_2_09_49_AM.png" alt="Screen_Shot_2017_08_07_at_2_09_49_AM" border="0"></a>

3. [copy pasta'd mostly from](https://github.com/rbarton65/espnff)

### To do

- make into web app
- add more features
