# Highlight Dates

Set day/days highlight, with different customizes.

## Usage

```js
const calendar = new HelloWeek({
  selector: '.calendar',
  langFolder: './langs/',
  todayHighlight: false,
  onSelect: data => {
    const { date } = data;
    calendar.setDaysHighlight([
      {
        days: [date],
        events: [
          {
            title: 'Event 1'
          },
          {
            title: 'Event 2'
          }
        ],
        attributes: {
          style: {
            backgroundColor: '#04f'
          }
        }
      }
    ]);
    calendar.update();
  }
});
```

## Demonstration

<iframe
    src="docs/v3/demos/highlights.html"
    frameborder="no"
    allowfullscreen="allowfullscreen">
</iframe>
