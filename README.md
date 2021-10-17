# weather

This program returns the weather.
It can also be returned as a bool type for comparison.

## How to use

### install

```shell
$ git clone https://github.com/moka-drip/weather.git
$ cd weather
$ pip install -e .
```

### programTest `weather`
```shell
$ weather
> Hi! weather is working properly.
```

## functions
How is the weather today.
```shell
$ weather today
> sunny / rainy / cloudy / etc...
```
How was the weather yesterday.
```shell
$ weather yesterday
> sunny / rainy / cloudy / etc...
```

## boolPrograms
```python
import weather

weather.{day} = {weather}  # <- boolType.
# {day} =today / yestarday / tomorrow  
# {weather} = sunny /rainy / cloudy / etc ...
```

## license
MIT

