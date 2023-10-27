
# Page Rank

Implemented the PageRank algorithm, calculating the "importance" of various Wikipedia pages.

Project completed for the “Cloud Computing” exam.


## Short Description

PageRank serves as an evaluation of web page quality by considering the **hyperlink graph's structure**. While Google's search algorithm takes into account numerous features, PageRank stands out as one of the most renowned and extensively studied.

To vividly illustrate PageRank, envision a **random web surfer**: this surfer lands on a page, randomly selects a link, and repeats this process endlessly. PageRank quantifies how frequently a page would encounter this tireless web surfer. More precisely, it's a probability distribution across nodes in the graph, indicating the likelihood of a random walk within the link structure arriving at a specific node. Nodes with high in-degrees tend to possess elevated PageRank values, as do nodes linked to by other nodes with high PageRank values. This behavior aligns with our expectations: high-quality pages are anticipated to have numerous endorsements from other pages in the form of hyperlinks. Likewise, if a high-quality page links to another, the second page is likely to be of high quality too.

The comprehensive PageRank formulation introduces an additional component. The web surfer doesn't click links randomly. Instead, a biased coin is flipped before each move. If it's heads, the surfer clicks on a random link, but if it's tails, the surfer ignores the page's links and teleports to a completely different page.

PageRank's recursive nature leads to an iterative algorithm structurally akin to parallel breadth-first search. This program works with pages from the Simple English Wikipedia, calculating the "importance" of various Wikipedia pages based on the PageRank metric and presenting them in descending order of importance. The data source is a pre-processed version of the Simple Wikipedia corpus, stored in XML format.
