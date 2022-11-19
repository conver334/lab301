---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# FACULTY
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: faculty"
%}
{:.center}
# PH.D STUDENT
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{:.center}
# M.SC STUDENTS
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: master"
%}
{:.center}
# ALUMNI
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: alumni"
%}
{:.center}
