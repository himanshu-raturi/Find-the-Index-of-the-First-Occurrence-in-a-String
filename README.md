# 28. Find the Index of the First Occurrence in a String

## Problem Description
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Approach
Both the Python and C++ solutions utilize their language's standard library string search functions (`find()`). These built-in methods are highly optimized and typically implement variants of efficient string matching algorithms (like Boyer-Moore or Two-Way string matching).

## Solutions Provided
- `solution.py`: Python 3 solution using `haystack.find(needle)`.
- `solution.cpp`: C++ solution using `std::string::find()`.

## Complexity
- **Time Complexity:** $O(N \times M)$ in the worst case (where $N$ is the length of `haystack` and $M$ is the length of `needle`), but $O(N)$ on average due to language-level optimizations.
- **Space Complexity:** $O(1)$ since no additional space scaling with input size is used.
