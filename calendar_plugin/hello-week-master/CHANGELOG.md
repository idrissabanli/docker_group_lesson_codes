## Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

#### [2.10.3] - 2019-08-01

**Changed**

- Fix issue [#29](https://github.com/mauroreisvieira/hello-week/issues/29) `range` option.
- Fix issue [#26](https://github.com/mauroreisvieira/hello-week/issues/26) timezone.

---

#### [2.10.1] - 2019-05-09

**Changed**

- Fix issue [#23](https://github.com/mauroreisvieira/hello-week/issues/23) `setDayHighlight()` method.

---

#### [2.4.0] - 2019-03-22

**Changed**

- Fix issue [#20](https://github.com/mauroreisvieira/hello-week/issues/20) `getDays()` method.

---

#### [2.3.0] - 2019-03-19

**Changed**

- Fix issue [#20](https://github.com/mauroreisvieira/hello-week/issues/20) `setDaysHighlight()` method.

---

#### [2.2.0] - 2019-03-17

**Changed**

- Fix issue [#19](https://github.com/mauroreisvieira/hello-week/issues/19) `setDaysHighlight()` method.

---

#### [2.1.0] - 2019-02-24

**Added**

- Option `daysSelected` set day/days selected [#13](https://github.com/mauroreisvieira/hello-week/issues/13).
- Italian translation. Thanks [@roland-d](https://github.com/roland-d).
- Updated Documentation.

**Changed**

- Fix issue [#16](https://github.com/mauroreisvieira/hello-week/issues/16) `goToDate()` method.

---

#### [2.0.0] - 2019-01-28

**Added**

- Method `setRange` toggle status of range..
- Method `setLocked` set calendar locked.
- Option `rtl` allows layout for languages written from right to left (like Hebrew or Arabic).
- Option `locked` sets all days of the week locked.
- Documentation for Customization your own theme.

**Changed**

- Fix issue [#10](https://github.com/mauroreisvieira/hello-week/issues/10) month date range.
- Updated Documentation.

---

#### [1.4.1] - 2018-06-18

**Added**

- Spanish translation. Thanks [@8geonirt](https://github.com/8geonirt).

**Changed**

- Fix `defaultDate` option also minDate and maxDate. Thanks [@8geonirt](https://github.com/8geonirt).
- Updated demos.

---

#### [1.4.0] - 2018-05-23

**Added**

- Option `nav` show next/prev buttons.

---

#### [1.3.2] - 2018-05-15

**Changed**

- Fix method used in option `range` to ignore dates lower than the first selected date.

---

#### [1.3.1] - 2018-05-08

**Changed**

- Fix changelog.

---

#### [1.3.0] - 2018-05-08

**Added**

- Option `range` allows you to select array range of days.
- Method `setRange()` toggle status of range.

---

#### [1.2.0] - 2018-04-30

**Added**

- Option `daysHighlight` accepted object or array of objects to make days with highlight.

---

**Changed**

- Fix `defaultDate` option when don't have `format` defined.

---

#### [1.1.0] - 2018-04-25

**Added**

- Method `today()` move the calendar to current day.
- Method `getToday()` get current day with the format if specified, timestamp in another case.
- Method `clear()` clean yours selected days in calendar.
- View documentation in demos folder.

**Changed**

- Webpack version (4.6.0).
- Typescript version (2.8.1).

---

#### [1.0.0] - 2018-04-12

**Added**

- Option `weekStart` define day of the week start. 0 (Sunday) to 6 (Saturday).

---

#### [0.1.0] - 2018-04-12

**Added**

- Option `todayHighlight`
- Option `disableDaysOfWeek` accepted array number.
- Option `disableDates` accepted array with days and also array of arrays.
- Option `langFolder` define path of langs folder.

---

#### [0.0.6] - 2018-04-10

**Added**

- Portuguese/Brazilian translation. Thanks [@fontebasso](https://github.com/fontebasso).

---

#### [0.0.5] - 2018-04-10

**Added**

- Option `defaultDate` to permit user define the initial date in HelloWeek.

---

**Changed**

- Fix order of days in the week on langs folder.

---

#### [0.0.4] - 2018-03-10

**Added**

- Option `minDate` define min date possible to select in HelloWeek.
- Option `maxDate` define max date possible to select in HelloWeek.
- Option `format` can you define the format of days in HelloWeek.
- Package in yarn & npm
- Version navigation.

---

#### [0.0.3] - 2018-03-10

**Added**

- Option `lang` define language of HelloWeek.
