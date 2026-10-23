# Exam 1 Part 2 In Class Practice Guide

## Purpose

This activity gives you a timed rehearsal of the practical-exam workflow using a different dataset and different questions. Focus on choosing methods from variable types, writing readable code, inspecting output, and explaining evidence in context.

## Files

Place these files together in `02-exams/exam-1/`:

- `Exam1_Part2_Practice.ipynb`
- `auto_mpg_practice.csv`

Open the course root in VS Code, open the practice notebook, and confirm that its working directory can locate `auto_mpg_practice.csv` with a relative path.

## Suggested Thursday Schedule

- **First 5 minutes:** Open the files, select the correct kernel, read the data dictionary, and confirm the CSV path.
- **Next 10 minutes:** Complete Question 1 and identify each later question's variable types before choosing a graph.
- **Next 20 minutes:** Complete Questions 2-6. Keep code direct and label each finished graph immediately.
- **Next 15 minutes:** Complete as much of Question 7 as possible. Prioritize correct `X` and `y` shapes, fitting, prediction, metrics, and interpretation.
- **Final 5 minutes:** Restart the kernel, run all cells, inspect the outputs, and test the HTML export.

Question 8 is optional if the timed work is complete.

## Working Strategy

I. Translate the prompt into the required evidence before coding: a table, graph, metric, interpretation, or combination.

II. Identify whether each variable is qualitative or quantitative in context. Numeric storage does not automatically make a variable quantitative.

III. Prepare only the columns and complete rows needed for the current task. Recheck the resulting shape after removing missing values.

IV. Construct the simplest suitable graph first. Add titles, axis labels, units, category order, and legends after confirming the marks are correct.

V. Interpret what the output shows. Include direction, differences, typical values, variation, or limitations only when they are supported by the display or metric.

VI. For regression, check the dimensions of `X` and `y`, interpret the slope in units, distinguish fitted values from guaranteed outcomes, and remember that in-sample metrics do not prove future performance.

## Skills Checklist

- Load a CSV with a relative path.
- Inspect rows, shape, columns, data types, and missing values.
- Build one-way and two-way frequency tables.
- Choose between bar charts, histograms, scatterplots, and box plots.
- Use ordering and color only when they support the comparison.
- Create a two-dimensional predictor table and one-dimensional response.
- Fit and inspect `LinearRegression`.
- Generate fitted values and a new prediction.
- Calculate and interpret MAE and R-squared.
- Diagnose observed-versus-predicted values with an identity line.
- State limitations and avoid unsupported causal or future-performance claims.

## End of Practice Reflection

After the timed attempt, mark each question as:

- **Ready:** completed correctly without notes.
- **Review:** completed after consulting a lab or study guide.
- **Repractice:** could not complete or interpret confidently.

Use those marks to decide which Lab 1-6B examples to revisit before the exam.
