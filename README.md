# Linked List Animation

A simple Manim project that visualizes a linked list by animating numbered nodes and directional arrows between them.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Manim](https://img.shields.io/badge/Manim-Animation-FF6B6B?style=for-the-badge)

## Overview

This project demonstrates a linked list as a sequence of nodes labeled 1 through 5. Each node is created and connected with arrows to show how data flows from one element to the next.

## Features

- Animated node creation
- Connected arrow links between elements
- Clean educational visualization for data structures
- Built with Manim for smooth motion and presentation

## Project Structure

```text
.
├── link-list.py
├── media/
│   ├── images/
│   └── videos/
└── README.md
```

## Requirements

- Python 3.8+
- Manim

## Installation

```bash
pip install manim
```

If you are using a virtual environment, activate it first and then install Manim.

## Run the animation

From the project folder, run:

```bash
python -m manim -pqk -r 1920,1080 link-list.py Linklist
```

This renders the scene and generates the output inside the `media/` folder.

## Notes

- The scene class is named `Linklist`.
- The output is saved under the `media` directory by default.
- This is a beginner-friendly example for learning how to animate data structures with Manim.

## License

This project is intended for educational and learning purposes.
