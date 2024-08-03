# langgraph_ai_content_researcher

![Screenshot 2024-08-03 125841](https://github.com/user-attachments/assets/6cc4f3be-196b-46ae-a025-87e95ef45f82)

shown above is the graph of all the agent nodes present within the project. here's a brief description of each - 

1. __start__ : signifies beginning of the graph, control first enters here.
2. PLANNER NODE: Given a user-prompt, this agent will create a rough skeleton of sub-topics, to generate content on for the article.
      example: Task: "Write a content article on the men's singles competition in tennis at the 2024 Paris Olympic games"
      planner:
  "plan:
    I. Introduction
    A. Brief overview of the significance of tennis in the Olympics
    B. Introduction to the men's singles competition at the 2024 Paris Olympic games

II. History of Men's Singles Tennis at the Olympics
    A. Evolution of tennis as an Olympic sport
    B. Notable moments in men's singles tennis at past Olympic games

III. Players to Watch in the 2024 Paris Olympics
    A. Top-ranked players expected to compete
    B. Rising stars and dark horses in the competition

IV. Key Matches and Results from the 2024 Paris Olympics
    A. Analysis of pivotal matches
    B. Breakdown of the medal rounds

V. Impact of the 2024 Paris Olympics on Men's Singles Tennis
    A. Influence on the players' careers
    B. Implications for the future of men's singles tennis

VI. Conclusion
    A. Recap of the significance of the men's singles competition at the 2024 Paris Olympics
    B. Final thoughts on the event and its impact on the sport of tennis."

3. RESEARCH_PLAN NODE: Given a plan as input, it will look up topics relevant to the plan using the Tavily search engine, and present findings.
     example:
     research_plan:
  content:
    ["Timing and scoring provided by OMEGA. Results powered by Atos. In case you missed it. Official competition schedule and live results for Tennis - Men's Singles at the Paris 2024 Olympics (Jul 26-Aug 11, 2024)", "Spain's Carlos Alcaraz defeated the Netherlands' Tallon Griekspoor 6-1 7-6 (3) Monday to reach the third round of the Paris Games tennis tournament. Live scores for the 2024 Olympics Men's Singles ...", "Top three seeds Novak Djokovic, Carlos Alcaraz and Alexander Zverev are into the quarter-finals of the men's singles tournament at Paris 2024 after victories on Wednesday 31 July.. Djokovic and Alcaraz, seeking their first Olympic gold medals, are on a collision course should they survive their next two assignments for a potential mouth-watering final clash.", "The Sporting News collates the draws for the men's and women's 2024 singles. MORE: Tennis at Olympics 2024: List of players competing at the Paris Games. When are the tennis events at the Paris ...", "Spain's Carlos Alcaraz defeated the Netherlands' Tallon Griekspoor 6-1 7-6 (3) Monday to reach the third round of the Paris Games tennis tournament. Live scores for the 2024 Olympics Men's Singles ...", "27. Show Live Matches (1) Paris 2024 Olympics. Court Philippe-Chatrier. Men's Singles - Round of 32. Alexander Zverev (Germany) beat Tomas Machac (Czech Republic) Result. 1. 2."]

4. GENERATE NODE: Given plan and research_material as input, it will generate a draft.
   example:
   generate:
  draft:
    **Title: The Thrilling Men's Singles Tennis Competition at the 2024 Paris Olympics**

I. **Introduction**
Tennis has always held a special place in the Olympics, showcasing the finest skills and sportsmanship on a global stage. The men's singles competition at the 2024 Paris Olympic Games continues this tradition, bringing together top athletes from around the world to compete for the coveted gold medal.

II. **History of Men's Singles Tennis at the Olympics**
Since its reintroduction as a full medal sport in 1988, men's singles tennis at the Olympics has witnessed remarkable moments that have etched themselves into the annals of sporting history. From Andre Agassi's gold in 1996 to Andy Murray's consecutive victories in 2012 and 2016, the event has seen legends rise and new stars emerge.

III. **Players to Watch in the 2024 Paris Olympics**
The 2024 Paris Olympics feature a stellar lineup of top-ranked players, including the likes of Novak Djokovic, Carlos Alcaraz, and Alexander Zverev. These seasoned competitors bring a wealth of experience and skill to the court, setting the stage for intense battles and thrilling matches. Keep an eye out for rising stars and dark horses who might just upset the established order.

IV. **Key Matches and Results from the 2024 Paris Olympics**
As the competition unfolds, fans can expect nail-biting encounters and edge-of-the-seat action. Pivotal matches will determine the course of the tournament, leading up to the medal rounds where the best of the best will vie for Olympic glory. Stay tuned for in-depth analysis and breakdowns of these crucial matchups. 

V. **Impact of the 2024 Paris Olympics on Men's Singles Tennis**
The 2024 Paris Olympics will not only shape the careers of the players involved but also have far-reaching implications for the future of men's singles tennis. The lessons learned, experiences gained, and rivalries forged during this event will resonate throughout the tennis world, influencing the trajectory of the sport for years to come.

VI. **Conclusion**
In conclusion, the men's singles competition at the 2024 Paris Olympics promises to be a spectacle of skill, determination, and passion. As the world watches in anticipation, we can expect unforgettable moments, fierce competition, and a celebration of the enduring spirit of tennis. Let us embrace this event and revel in the magic it brings to the sport we love.

5. REFLECT NODE: acts as a critique of the generated content; points out redundancies and suggests improvements on the article.
  example:
reflect:
  critique:
    **Overall Feedback:**
The essay provides a solid overview of the men's singles tennis competition at the 2024 Paris Olympics. The structure is clear, with sections covering the introduction, history, players to watch, key matches, impact, and conclusion. However, there are areas where the essay could be improved to enhance its depth and engagement.

**Content and Depth:**
1. **Introduction:** The introduction effectively sets the stage for the discussion but could benefit from a more engaging hook to capture the reader's attention. Consider incorporating a compelling anecdote, statistic, or quote related to men's singles tennis at the Olympics.

2. **History of Men's Singles Tennis at the Olympics:** While the historical overview is informative, consider expanding on specific iconic moments or controversies in men's singles tennis at the Olympics. Provide more detailed insights into the evolution of the event and its significance in the tennis world.        

3. **Players to Watch in the 2024 Paris Olympics:** The section on players to watch is a highlight of the essay. To enhance this section, include brief player profiles highlighting their strengths, playing styles, and recent achievements. This will provide readers with a deeper understanding of the competitors.      

4. **Key Matches and Results from the 2024 Paris Olympics:** While mentioning pivotal matches is crucial, consider delving into potential matchups, rivalries, and predictions for the tournament. Analyze the playing styles of key players and how they might influence match outcomes.

5. **Impact of the 2024 Paris Olympics on Men's Singles Tennis:** This section has potential but lacks specific examples or insights into how the outcomes of the 2024 Paris Olympics could shape the future of men's singles tennis. Consider discussing potential rule changes, player endorsements, or the impact on the global tennis landscape.

**Style and Tone:**
1. **Engagement:** To enhance reader engagement, consider incorporating vivid descriptions, quotes from players or experts, and a more conversational tone throughout the essay. This will make the content more compelling and immersive for the audience.

2. **Analysis:** Encourage critical analysis by providing in-depth evaluations of players, matches, and the broader implications of the 2024 Paris Olympics on men's singles tennis. Offer unique perspectives, comparisons with past Olympics, and insights into the sport's evolution.

**Recommendations:**
1. **Length:** Consider expanding on each section to provide more detailed insights, analysis, and examples. Aim for a word count of at least 1000-1500 words to cover the topic comprehensively.

2. **Research:** Incorporate statistics, quotes from players or experts, and references to enhance the credibility and depth of the essay. Conduct thorough research on past Olympics, player backgrounds, and current tennis trends.

3. **Visuals:** To break up the text and enhance visual appeal, consider including images of players, match highlights, or infographics showcasing key statistics or matchups.

4. **Conclusion:** Strengthen the conclusion by summarizing key points, offering a reflective insight into the significance of the 2024 Paris Olympics, and leaving the reader with a thought-provoking takeaway.   

By implementing these recommendations and enhancing the content, depth, and style of the essay, you can create a compelling and informative piece that captivates readers and showcases your passion for men's singles tennis at the 2024 Paris Olympics.

6. RESEARCH_CRITIQUE NODE: Given the critique content, makes more tavily searches for relevant content from critique.
example: research_critique:
  content:
    ["Timing and scoring provided by OMEGA. Results powered by Atos. In case you missed it. Official competition schedule and live results for Tennis - Men's Singles at the Paris 2024 Olympics (Jul 26-Aug 11, 2024)", "Spain's Carlos Alcaraz defeated the Netherlands' Tallon Griekspoor 6-1 7-6 (3) Monday to reach the third round of the Paris Games tennis tournament. Live scores for the 2024 Olympics Men's Singles ...", "Top three seeds Novak Djokovic, Carlos Alcaraz and Alexander Zverev are into the quarter-finals of the men's singles tournament at Paris 2024 after victories on Wednesday 31 July.. Djokovic and Alcaraz, seeking their first Olympic gold medals, are on a collision course should they survive their next two assignments for a potential mouth-watering final clash.", "The Sporting News collates the draws for the men's and women's 2024 singles. MORE: Tennis at Olympics 2024: List of players competing at the Paris Games. When are the tennis events at the Paris ...", "Spain's Carlos Alcaraz defeated the Netherlands' Tallon Griekspoor 6-1 7-6 (3) Monday to reach the third round of the Paris Games tennis tournament. Live scores for the 2024 Olympics Men's Singles ...", "27. Show Live Matches (1) Paris 2024 Olympics. Court Philippe-Chatrier. Men's Singles - Round of 32. Alexander Zverev (Germany) beat Tomas Machac (Czech Republic) Result. 1. 2.", 'There are several popular hooks for sports-related essays: Quotations. A quotation is an engaging way to introduce your reader to the topic. Make sure the quote is relevant to the rest of the essay. "You have to expect things of yourself before you can do them." - Michael Jordan; Fun Facts. Use some fun or unexpected info about sports to ...', "Hooks can draw audiences in and persuade them to read your work more deeply. In this blog, we will examine the significance of powerful article hooks in content writing, understand their role in engaging readers, and give examples of powerful hooks used by news articles. Let's unlock the secrets to crafting compelling introductions! Figure 1.", "Serbia's Novak Djokovic returns to Italy's Lorenzo Musetti during their men's singles semi-final tennis match on Court Philippe-Chatrier at the Roland-Garros Stadium during the Paris 2024 Olympic ...", "He won the match 6-1, 6-1 to become only the fourth Spanish man to reach an Olympic singles final. In 1904, USA's Robert LeRoy reached the Olympics men's singles final at the age of 19.", "Tennis at Paris 2024 is heating up. No. 1 seed Novak Djokovic has powered into the Olympic tennis quarter-finals and looks to be the one to beat on the men's side.", "Top three seeds Novak Djokovic, Carlos Alcaraz and Alexander Zverev are into the quarter-finals of the men's singles tournament at Paris 2024 after victories on Wednesday 31 July.. Djokovic and Alcaraz, seeking their first Olympic gold medals, are on a collision course should they survive their next two assignments for a potential mouth-watering final clash."]

This research is then reverted back to the generator node, which will then generate again based on the info presented by research_critique node. 

NOTE: Any particular logic can be used to judge how many times the generated content needs to be critiqued. For the time being i have used a simple loop pointer which critiques every article 2 times.


