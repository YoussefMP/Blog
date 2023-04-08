import 'https://flackr.github.io/scroll-timeline/dist/scroll-timeline.js';

const scrollTracker = document.querySelector('.scroll-tracker');

const animatedDate = document.querySelector('.animated-date');

const animatedDateTimeline = new ScrollTimeline({
  scrollOffset: [
    {target: animatedDate, edge: "end", threshold: "1"},
    {target: animatedDate, edge: "start", threshold: "1"}
  ],
});

animatedDate.animate(
    {
        transform: ["perspective(500px) rotate(360deg)", "perspective(500px) rotate(0deg)"]
    },
    {
        duration: 1,
        timeline: animatedDateTimeline
    },
)