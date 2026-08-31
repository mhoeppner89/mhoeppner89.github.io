# Political Targets and Choice Under Uncertainty

*Evidence from German and U.S. Political Actions and Senate Campaign Appeals*

**Author:** Martin Höppner. Brandenburg University of Technology Cottbus--Senftenberg. Email: [martin.hoeppner@b-tu.de](mailto:martin.hoeppner@b-tu.de).

**Date:** August 2026

## Abstract

Politicians face goals such as winning an election, gaining enough votes to enter parliament, or keeping enough support to hold a coalition together. These rewards change how attractive uncertain actions are. An actor just below a target rationally accepts new ways to lose in exchange for a chance of a large gain. Being above favors protecting that advantage, while withdrawal might be optimal if there is no plausible route to success. This can create a public problem when winning matters more to a politician than preserving democratic institutions or voter approval. I use a simple model to separate the value of crossing a political target from an action's other consequences and from its value to the public. I examine 1,003 documented political actions in Germany and the United States from 2005 to 2026, and 4,291 first uses of distinct templates in U.S. Senate campaign emails in 2022 and 2024. Across the two action collections, all six position comparisons point in the predicted direction. A separate email study finds more language about large possible gains among forecast underdogs. These descriptive associations do not reveal private beliefs, establish a lower expected-value choice, or identify a causal effect. I conclude with possible institutional safeguards.

**Keywords:** political incentives; targets; choice under uncertainty; elections; democratic design

**JEL classification:** D72; D81; P16

empty

## Introduction

In a winner-takes-all election, 49.9 and 50.1 percent of the vote can bring very different political rewards. The difference in public support is small, yet the difference between office and opposition may be large. Similar targets determine whether a party enters parliament, a coalition survives, or a bill passes. Political competition tries to align political actors to their citizens, but the actual institutions also change which uncertain actions political actors prefer.

Consider a football match. Late in an important game, a team that trails by one goal may send its goalkeeper forward for a corner and accept a greater chance of conceding another goal. A team that leads may instead keep its strikers back to protect its advantage. The objective has not changed. Position relative to the winning line has changed which action offers the better chance of success. If the coach receives most of the reward from winning while the club and its supporters bear much of the loss, the choice may also conflict with their interests.

Political targets create the same pattern. Just below a target, an action with a chance of a large gain can become attractive even when it also creates new ways to lose. Just above it, protecting an existing advantage can become attractive. When no plausible route to the target remains, withdrawal may be better than another gamble. The reward for success changes the payoff to uncertainty while the actor's underlying preferences remain stable [@march1988aspirations]. Electoral accountability can therefore discipline politicians and distort a particular choice at the same time [@maskintirole2004politician]. The misalignment problem arises when the politician receives much of the reward from success while citizens bear much of the cost of failure and forgone better alternatives. Figure 1 summarizes this argument.

> **Figure.** Position relative to a political target changes the appeal of uncertain actions. The resulting choice may differ from the action that leaves the public better off.

Two German cases make the contrast concrete. Before the 2025 election, the Free Democratic Party (FDP) stood near the 5 percent threshold for entering parliament. Its platform proposed crypto exchange-traded funds and opened the door to Bitcoin reserves at the European Central Bank and the Bundesbank [@fdp2025crypto]. The proposal offered a possible route to new voters while risking support among existing ones, but ultimately backfired. Friedrich Merz provides an example of protecting a narrow lead just above a target. In 2025, his coalition held 328 of 630 Bundestag seats, only twelve more than the required majority [@bundestag2025merzvote]. He promised an ``autumn of reforms'' while emphasizing the need for broad support [@merz2025reforms][^1]. An ifo assessment found that the coalition agreement retained costly pension commitments, sent central pension questions to a commission, and lacked adequate cost controls for health and care, foregoing meaningful reforms [@ifo2025coalition].

Some actions go further by attacking the rule that determines political survival. The U.S. House January 6 Committee documented Donald Trump's effort to stop Congress from certifying the electoral result after his defeat [@jan6committee2022]. South Korea's Constitutional Court found that President Yoon Suk-yeol, whose support had declined and who faced possible impeachment [@ap2024yooncontext], used martial law without the required substantive or procedural basis during his conflict with the National Assembly; it removed him from office [@koreacourt2025yoon]. These extreme cases illustrate highly risky attempts to change the rules of political survival with significant impact on democratic processes.

Earlier work establishes the basic underdog--favorite result.[@rose1991risk] shows that, with expected electoral support held fixed, a plurality-election underdog may prefer a wider spread of possible vote shares while a favorite prefers a narrower one.[@lizzeripersico2009risk] show that winner-take-all electoral rules strengthen incentives to choose risky platforms relative to proportional rules.[@krakelniekenprzemeck2014risk] add campaign investment and laboratory evidence. A similar pattern appears outside politics when trailing mutual-fund managers increase portfolio volatility because rank affects compensation [@brown1996tournaments]. The general logic echoes Goodhart's law: once a measure becomes a target, efforts to control it can change the behavior that made it informative [@goodhart1975problems].

My theory explores risk behavior as a mechanism to ``game'' the political targets. Actors can adapt their choices to cross or protect a target. If they do so by sacrificing policy value, credibility, or democratic rules, the choice may reduce approval and trust and, in extreme cases, contribute to democratic backsliding. The paper connects political targets to three responses: risk taking below a target, protection above it, and withdrawal when success appears remote. It applies the same terms to electoral, legislative, coalition, party, and office targets. It also shows how an actor below a target may try to gain or preserve power through a highly volatile attempt to change the rule itself, and it keeps the politician's payoff separate from public welfare. The empirical studies test the predicted actions and campaign language.

## Political Choice Around Targets

### A simple choice

An action can be worse in every respect except its chance of crossing a political target and still be attractive when success is valuable enough. Suppose a political actor chooses an action $ a $. The action produces an uncertain political outcome $ X_a $, such as vote share, seats, coalition support, or legislative votes. Let $ \theta $ be the target. The actor's perceived chance of success is

$$
p_A(a)=\Pr_A(X_a\geq \theta).
$$

Let $ R_A(a) $ be the actor's expected payoff from every consequence other than the prize for crossing the target. It can include policy, reputation, resources, and political support, evaluated using the actor's beliefs. Let $ B>0 $ be the value of winning, remaining in office, or reaching the relevant political goal. The benchmark treats $ B $ as fixed across the actions being compared, so target success is not counted again in $ R_A(a) $. The actor's expected payoff is

$$
U_A(a)=R_A(a)+B p_A(a).
$$

For two actions,$ a $ and $ b $, the actor chooses $ a $ when

$$
\Delta U_A=\Delta R_A+B\Delta p_A\geq 0,
$$

where each difference is the value under $ a $ minus the value under $ b $. If $ a $ has worse consequences apart from target success,$ \Delta R_A<0 $, but a better chance of success,$ \Delta p_A>0 $, it remains attractive when

$$
B\geq \frac{-\Delta R_A}{\Delta p_A}.
$$

The public may rank the same actions differently. Let $ Q(a) $ be the expected public value of the policy and institutional consequences, let $ p_P(a) $ be the success probability used for the public-welfare comparison, and let $ G $ be the public value of that political result. Then

$$
W(a)=Q(a)+G p_P(a).
$$

For two actions,$ \Delta W=\Delta Q+G\Delta p_P $. A conflict exists when the politician prefers $ a $, so $ \Delta U_A\geq0 $, while the public-welfare comparison favors $ b $, so $ \Delta W<0 $.

The core logic is that target position changes the value of uncertainty. Consider two actions with the same expected result but different levels of volatility. For an underdog, a wider range of outcomes is often preferable because it increases the probability of a gain sufficient to cross the target. For a leader, that same volatility is less attractive because it increases the probability of losing the lead. While other factors such as policy preferences or reputational concerns also shape political choices, the target position specifically shifts the incentives surrounding risk. Figure 2 illustrates these two cases. Because we cannot observe a politician's private calculations or their exact perception of risk, I instead ask whether documented risk taking is more common among underdogs and protection is more common among leaders[^2].

> **Figure.** Political choices pivot on a vote threshold $ \theta $. Below it, politicians favor option $ A $ over $ B $ because it offers a better chance to win; above it, they favor option $ C $ over $ D $ because it lowers the risk of losing. This leads to on average worse performance that might contribute to trust erosion in the system favoring this behavior.

### Multiple targets, withdrawal, and changing rules

Political actors often face more than one goal simultaneously. A candidate may need to secure both the support of the general public and the approval of their party, while a chancellor may balance policy goals against the need to keep a coalition intact. The logic of risk changes depending on whether these goals are independent or joint. If winning one goal provides a separate reward, the actor treats them as separate prizes. However, if the actor must achieve all goals to receive any reward (such as needing both a legislative majority and a coalition's blessing to govern) the goals become a joint target. In these cases, the ``force'' of the target remains the same even if it is described using different labels.

The model can also account for the decision to stop trying. Every political pursuit has an ``outside option'', i.e. the value of directing effort elsewhere. An actor continues to pursue a target as long as the best expected payoff from continuing outweighs the value of giving up. The three-part pattern identified in the study suggests that as a target becomes more remote, the expected return from continued pursuit eventually falls below the value of walking away.

Finally, some actors may attempt to change the rules of the contest itself. When the standard path to a goal is blocked, an actor may take a highly uncertain action to achieve a higher-level objective, such as staying in office, by altering the conditions for success. This might involve changing the rules of certification or the requirements for martial law. The Trump and Yoon cases illustrate extreme attempts to redefine the conditions of success when the conventional path to power is no longer viable. Such actions may damage public trust or democratic institutions.

### Observable implications

Under these conditions, the model gives four observable patterns:

1. Risk taking should be more common just below a target than just above it.
2. Protection should be more common just above a target than just below it.
3. Withdrawal should be more common far below a target than close below it.
4. Higher stakes increase willingness to sacrifice non-target outcomes.
5. Campaigns classified by public forecasts as underdogs should mention the possibility of a large electoral gain more often than forecast leaders, if their public messages reflect this incentive.

The first four predictions concern documented actions. The fifth is a separate prediction about language. All require observed pre-action position to be a reasonable proxy for the actor's situation, a meaningful reward from target success, and relevant actions to be available.

## Evidence

I use three observational studies. Two compare political actions below, above, and far below electoral or office targets in Germany and the United States. The third asks whether U.S. Senate campaigns behind in public forecasts speak about large possible gains more often than campaigns ahead. The studies test whether recorded actions and language vary in the predicted direction.

### Political actions in Germany and the United States

I examine 1,003 documented political actions across 2005--2026, spanning municipal, state, and national politics in Germany and the United States. The cases are documented examples, not a representative sample of every political move. Cases were included because a responsible actor took a documented action linked to an electoral or office target, not because of what happened later. Only information available before the action is used to determine the actor's target, position, and action.

I record three yes-or-no features of each action. They can overlap:

- *Risk taking*: the action creates both a new possible gain and a new possible loss, as when a campaign replaces a familiar message with an untested appeal.
- *Protection*: the action gives up a specific opportunity to block a concrete threat, as when a government shelves a reform that might endanger a narrow coalition majority.
- *Withdrawal*: the actor stops pursuing the target, as when a candidate ends a campaign rather than continuing an implausible effort.

I use the same comparisons in both countries. For risk taking, I compare actors close below with actors close above. For protection, I reverse that comparison. For withdrawal, I compare actors far below with actors close below. The action-comparison table reports the differences and p-values.

> **Caption.** Position and observed action patterns

| Action and comparison | Difference | $ p $-value |
| --- | --- | --- |
| *Germany* |  |  |
| Risk taking: close below vs. close above | $+12.6 $ pp | $ 0.042 $ |
| Protection: close above vs. close below | $+2.8 $ pp | $ 0.070 $ |
| Withdrawal: far below vs. close below | $+16.5 $ pp | $ 0.043 $ |
| *United States* |  |  |
| Risk taking: close below vs. close above | $+14.6 $ pp | $ 0.019 $ |
| Protection: close above vs. close below | $+16.9 $ pp | $<0.001 $ |
| Withdrawal: far below vs. close below | $+68.3 $ pp | $<0.001 $ |

> **Caption.** Notes: Differences subtract the second position from the first. P-values are one-sided in the direction predicted by the theory and account for repeated observations of the same actor and political target. The estimates are descriptive. Appendix Methods reports additional checks.

All six raw differences point in the predicted direction with the U.S. protection and withdrawal differences being the clearest. The German protection comparison contains only two events ($ p=0.070 $). German withdrawal also depends on the kinds of targets in the sample. The raw difference is 16.5 percentage points, but it falls to 7.7 points when both positions are compared using the same mix of target types. Within the dominant proportional or legislative group, the difference is about half a percentage point. The German result therefore does not establish a general tendency to withdraw from distant targets.

The next question is whether the action differences become larger under pressure. I call stakes high when the actor faces a high or exceptional personal consequence, such as losing office or failing to enter parliament. The answer is mixed. In the United States, all three differences are larger among high-stakes cases, although the lower-stakes groups are small. Germany shows no common pattern: higher stakes strengthen the risk-taking difference, barely change protection, and reverse the withdrawal difference. A deadline of 30 days or less also fails to strengthen the three differences consistently. Germany lacks an exact deadline in 189 of 500 cases, so its deadline checks are especially tentative (see Appendix Action checks).

An action counts as accepting sacrifice when the pre-action record shows policy value, reputation, resources, or average political support put at risk or given up. Such sacrifice appears in 70.8 percent of high-stakes German cases and 58.6 percent of lower-stakes cases, a difference of 12.2 percentage points ($ p=0.006 $). The corresponding U.S. rates are 36.0 and 23.3 percent, a difference of 12.8 points ($ p=0.014 $). Yet sacrifice does not rise steadily across the four stake categories. Deadline results also depend on where the line is drawn. At 90 days, the shorter-deadline difference is 11.6 points in Germany ($ p=0.051 $) and 13.6 points in the United States ($ p=0.018 $). But at 30 days, it is $-1.4 $ points in Germany ($ p=0.583 $) and 2.7 points in the United States ($ p=0.338 $).

### U.S. Senate campaign appeals

The email study is a separate test of campaign language, not a direct test of political choice, but serves as an external dataset to test the discussed pattern. The Political Email Archive supplies processed fundraising messages [@willis2026politicalemails]; Federal Election Commission records identify candidate-authorized Senate campaigns [@fec2026]; and public forecasts show whether each campaign was ahead or behind before each message and serve as a proxy for the actor's position [@fivethirtyeight2022method; @morris2024forecast].

The archive contains 8,339 messages from the 2022 and 2024 election years. Campaigns often resend nearly identical text, so the analysis keeps only the first recorded use of each campaign template. After excluding identical templates, the ones without the required language or forecast measures, the sample contains 4,291 templates from 64 campaigns in 45 Senate contests (Table email-flow). A negative expected vote margin defines an underdog; a positive margin defines a leader.

The language measure records whether a template describes the possibility of a large electoral gain: for example, an upset, flipping a seat, or expanding a party majority. It captures public language about large possible gains[^3]. It does not measure the campaign's perceived spread of possible results or show that the campaign chose a riskier strategy.

The raw pattern appears in both years. In 2022, 15.0 percent of underdog templates mention a large possible gain, compared with 3.5 percent of leader templates. In 2024, the corresponding rates are 12.0 and 3.4 percent. After adjustment for forecast closeness, time to the election, incumbency, party, and year, the estimated rates are 9.8 percent for underdogs and 4.6 percent for leaders. The difference is 5.3 percentage points, with a 95 percent interval from 1.9 to 8.6 points.

Checks that group repeated observations by contest, give each campaign equal weight, isolate explicit terms such as *underdog* and *upset*, or account for routine fundraising language leave the main association positive. Appendix Email methods reports the models and checks.

This result is an across-campaign association, not evidence of a sharp change when a forecast crosses zero. Estimates near zero change with the chosen range, and the within-campaign comparison is imprecise. Stable differences in campaign writing may explain part of the pattern. Identifying an effect of forecast position would require stronger evidence, such as randomized messages or a credible source of movement in forecasts unrelated to campaign style.

## Institutional Implications

The three studies describe a common pattern: actors below a target take risks more often, actors above it protect an advantage more often, actors far below it withdraw more often, and forecast underdogs speak more often about large possible gains. The studies do not show that target position caused these responses. They also do not measure later public harm, public trust, or the effects of any reform. The proposals below therefore follow from the model. They matter when a political target gives the decision maker a large private reward and citizens bear much of the possible loss.

Democracy cannot abolish targets. Elections need winners, legislatures need decision rules, and governments need a way to survive or fall. The useful question is which targets create the greatest conflict. How abruptly support turns into power; how much personal or partisan value arrives at the target; who bears the downside of the action; and how easily a bad decision can be undone. A one-vote legislative majority is not automatically a problem, but it becomes more troubling when that one vote delivers control over many institutions, lets the winner alter the next contest, or permits an irreversible decision whose costs fall mainly on others.

**Reduce the size of the immediate prize.**The first design principle is to avoid giving one narrow victory control over everything. Winner-take-all rules create a more concentrated prize than proportional rules and can change both campaign risk and the kinds of benefits politicians offer [@lizzeri2001public; @lizzeripersico2009risk]. Proportional representation is not always preferable as concentrated authority can make responsibility clearer and government more decisive. But where a narrow win produces sweeping control, institutions can preserve meaningful influence for the losing side through committee access, information rights, agenda rights, or other formal powers. Such opposition powers vary substantially across legislatures [@wegmann2022opposition], and fair procedures are associated with greater political support among electoral losers [@martiniquaranta2019support].

Staggered terms or separately elected offices can also divide control over time. This only softens the immediate prize when the current contest settles part of future power. If every approval is required for one indivisible reward, adding more gates may simply create a harder joint target and more deadlock. The institutional question is therefore not how many votes occur, but how much control any one of them transfers.

**Protect the rules of the contest.**The second principle is to make it harder for current officeholders to alter the rule that determines their own survival. Rule changes can also protect an advantage from above, so this concern extends beyond the extreme cases discussed earlier. Independent administration, public reasons, review by another institution, and delayed implementation can separate a rule change from its immediate political payoff. In redistricting, for example,[@cox2006redistricting] proposes letting legislators draw plans while delaying their use for several elections. The delay weakens the link between today's map and the careers of the people drawing it. Yet, delay also has costs: it can preserve a defective rule or prevent a timely response to changed circumstances. A workable safeguard therefore needs a narrow route for urgent correction, with reasons stated publicly and approval by an actor that does not receive the immediate electoral benefit. The purpose is to review self-interested rule changes, not to freeze every rule forever.

**Make costly decisions easier to reverse.**The third principle is to limit irreversible losses when uncertainty is high. Pilot programs, staged authority, and expiry dates can let a government try a policy while preserving a route back. Policy variation can produce information, and reversibility allows later decisions to use what has been learned [@listokin2008learning]. A pilot should therefore specify its scale, the evidence to collect, and what happens when it ends. Otherwise a temporary program can quietly become permanent, or its renewal date can create another political cliff.

**Use citizen participation to reduce political misalignment.**When politicians prioritize self-preservation over public preferences, citizen initiatives and referendums offer a useful correction. A referendum lets voters block a rule change or costly policy without having to remove the official who proposed it. Likewise, an initiative forces a vote on proposals that representatives would rather delay. Theoretical work shows that even the possibility of a referendum can discipline politicians across decisions beyond the specific measures put to a vote [@lebihan2018referendum]. Comparative evidence suggests that direct democracy has its strongest effect where politicians and the public disagree most [@leemannwasserfallen2016democratic]. For this mechanism to work, the process must remain citizen-driven and legally binding; political control over the process can restore the conflict of interest [@chenevalelwakil2018referendums].

Direct democracy also creates another target. A binary referendum forces a complex policy debate into a yes-or-no choice, making wording and agenda control politically valuable. Clear access rules, neutral wording, and a single challenge period can limit this advantage. Where a policy allows for middle ground, the ballot could offer options such as the status quo, a limited pilot, a narrower reform, or the full proposal. Multi-option voting can reveal intermediate preferences, though the choice of options and counting rule can still affect the result [@wagenaar2019multioption]. Direct participation reduces one conflict of interest between voters and politicians but creates a new target that needs its own safeguards.

## Conclusion

Political targets do more than separate winners from losers. By making small differences in support decisive, they change which uncertain actions politicians prefer. An actor just below a target may accept new ways to lose for a chance of crossing it; an actor just above may give up other opportunities to protect a lead; and an actor with no plausible route to success may withdraw. These choices can be rational for politicians even when citizens would prefer a different course.

The patterns in recorded political actions and campaign language are consistent with this account. A repeated-choice experiment could isolate the mechanism. Participants could act as candidates choosing among a campaign that produces a wider spread of possible vote shares, one that protects their current support, and withdrawal. The experiment would vary whether they begin just below, just above, or far below the support needed to win, and how much they personally gain from victory.

Democracy needs decisive rules, but a narrow victory need not transfer every source of political power or expose citizens to irreversible losses. Institutional design can preserve accountability while limiting the prize attached to a single target, protecting the rules of competition, and keeping costly choices open to correction. Each safeguard also creates a target of its own and must be designed with the same incentives in mind.

##### Acknowledgment.

Generative AI tools were used extensively to shorten and clarify this manuscript. The author directed and reviewed each revision and remains responsible for the arguments, analysis, and any errors.

## References

- Associated Press. South korea lifts president's martial law decree after lawmakers reject military rule, December 2024. URL <https://apnews.com/article/997c22ac93f6a9bece68454597e577c1>. Accessed 28 August 2026.

- Keith C. Brown, W. V. Harlow, and Laura T. Starks. Of tournaments and temptations: An analysis of managerial incentives in the mutual fund industry. *Journal of Finance*, 51 (1): 85--110, 1996. 10.1111/j.1540-6261.1996.tb05203.x.

- Francis Cheneval and Alice el Wakil. The institutional design of referendums: Bottom-up and binding. *Swiss Political Science Review*, 24 (3): 294--304, 2018. 10.1111/spsr.12319.

- Constitutional Court of Korea. Case on impeachment trial of president (Yoon Suk-yeol), 2024Hun-Na8, April 2025. URL <https://isearch.ccourt.go.kr/view.do?docId=84503&idx=01>. Official decision in English, 4 April 2025.

- Adam B. Cox. Designing redistricting institutions. *Election Law Journal*, 5 (4): 412--424, 2006. URL <https://chicagounbound.uchicago.edu/journal_articles/9958/>.

- Federal Election Commission. Candidate master file description, 2026. URL <https://www.fec.gov/campaign-finance-data/candidate-master-file-description/>. Accessed 23 August 2026.

- FiveThirtyEight. How FiveThirtyEight's House, Senate and governor models work, 2022. URL <https://web.archive.org/web/20221108054504/https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/>. Forecast methodology. Archived 8 November 2022.

- Free Democratic Party. Einsatz von Kryptowährungen als Währungsreserven, 2025. URL <https://www.fdp.de/forderung/einsatz-von-kryptowaehrungen-als-waehrungsreserven>. Extract from the 2025 federal-election platform. Accessed 23 August 2026.

- Clemens Fuest. The coalition agreement: Implications for the German economy. ifo Institute, April 2025. URL <https://www.ifo.de/en/opinion/2025-04-25/coalition-agreement-implications-german-economy>. Accessed 23 August 2026.

- German Bundestag. Friedrich Merz mit 325 Stimmen zum Bundeskanzler gewählt, May 2025. URL <https://www.bundestag.de/dokumente/textarchiv/2025/kw19-de-kanzlerwahl-1062470>. Official election record. Accessed 23 August 2026.

- German Federal Government. Speech by chancellor Friedrich Merz on the 2025 budget act, September 2025. URL <https://www.bundesregierung.de/breg-de/service/newsletter-und-abos/bulletin/rede-von-bundeskanzler-friedrich-merz-2384970>. Official speech, 17 September 2025. Accessed 26 August 2026.

- Charles A. E. Goodhart. Problems of monetary management: The U.K. experience. In *Papers in Monetary Economics*, volume 1, pages 1--20. Reserve Bank of Australia, Sydney, 1975.

- Matthias Kräkel, Petra Nieken, and Judith Przemeck. Risk taking and investing in electoral competition. *European Journal of Political Economy*, 33: 98--120, 2014. 10.1016/j.ejpoleco.2013.12.003.

- Patrick Le Bihan. Popular referendum and electoral accountability. *Political Science Research and Methods*, 6 (4): 715--731, 2018. 10.1017/psrm.2016.41.

- Lucas Leemann and Fabio Wasserfallen. The democratic effect of direct democracy. *American Political Science Review*, 110 (4): 750--762, 2016. 10.1017/S0003055416000307.

- Yair Listokin. Learning through policy variation. *Yale Law Journal*, 118 (3): 480--553, 2008. 10.2307/20454719.

- Alessandro Lizzeri and Nicola Persico. The provision of public goods under alternative electoral incentives. *American Economic Review*, 91 (1): 225--239, 2001. 10.1257/aer.91.1.225.

- Alessandro Lizzeri and Nicola Persico. Electoral incentives, political risk-taking and policy reform. In Enriqueta Aragones, Carmen Bevia, Humberto Llavador, and Norman Schofield, editors, *The Political Economy of Democracy*, pages 193--218. Fundacion BBVA, 2009. URL <https://www.fbbva.es/wp-content/uploads/2017/05/dat/DE_2009_political_economy.pdf>.

- James G. March. Variable risk preferences and adaptive aspirations. *Journal of Economic Behavior & Organization*, 9 (1): 5--24, 1988. 10.1016/0167-2681(88)90004-2.

- Sergio Martini and Mario Quaranta. Political support among winners and losers: Within- and between-country effects of structure, process and performance in europe. *European Journal of Political Research*, 58 (1): 341--361, 2019. 10.1111/1475-6765.12284.

- Eric Maskin and Jean Tirole. The politician and the judge: Accountability in government. *American Economic Review*, 94 (4): 1034--1054, 2004. 10.1257/0002828042002606.

- G. Elliott Morris. How 538's 2024 Senate election forecast works. ABC News, October 2024. URL <https://abcnews.com/538/538s-2024-senate-election-forecast-works/story?id=114997770>. Accessed 23 August 2026.

- Susan Rose-Ackerman. Risk taking and electoral competition. *European Journal of Political Economy*, 7 (4): 527--545, 1991. 10.1016/0176-2680(91)90035-2.

- Select Committee to Investigate the January 6th Attack on the United States Capitol. Final report, 2022. URL <https://www.govinfo.gov/app/details/GPO-J6-REPORT/context>. Official report, 22 December 2022.

- Amos Tversky and Daniel Kahneman. Advances in prospect theory: Cumulative representation of uncertainty. *Journal of Risk and Uncertainty*, 5 (4): 297--323, 1992. 10.1007/BF00122574.

- Charlotte C. L. Wagenaar. Beyond for or against? multi-option alternatives to a corrective referendum. *Electoral Studies*, 62: 102091, 2019. 10.1016/j.electstud.2019.102091.

- Simone Wegmann. Policy-making power of opposition players: A comparative institutional perspective. *The Journal of Legislative Studies*, 28 (1): 1--25, 2022. 10.1080/13572334.2020.1843233.

- Derek Willis. Political email archive. GitHub repository, 2026. URL <https://github.com/dwillis/political-emails>. Accessed 26 August 2026.

## Appendix

## Formal Details

### A benchmark for the spread of political outcomes

Let the political outcome under action $ a $ be

$$
X_a=\mu_a+\sigma_a\varepsilon,
$$

where $ \mu_a $ is the expected outcome,$ \sigma_a>0 $ is its spread, and $ \varepsilon $ has a continuously differentiable cumulative distribution $ F $ with density $ f $. Define $ z_a=(\theta-\mu_a)/\sigma_a $. The actor's chance of crossing the target is

$$
p_A(a)=1-F(z_a).
$$

Holding the expected outcome and target fixed,

$$
\frac{\partial p_A}{\partial \sigma_a}
=\frac{f(z_a) z_a}{\sigma_a}.
$$

Where $ f(z_a)>0 $, a wider spread raises the chance of success when $ \mu_a<\theta $, lowers it when $ \mu_a>\theta $, and has no first-order effect when $ \mu_a=\theta $. The last case implies a 50-percent chance of success only when $ F(0)=1/2 $, as in a symmetric distribution centered at zero.

This result concerns the chance of target success, not the whole choice. Equation (choice) still requires the political prize to outweigh the action's other consequences. The benchmark also treats probabilities linearly. If actors overweight or underweight particular probabilities, as in cumulative prospect theory [@tversky1992advances], the prize term would need a probability-weighting function. The paper can not distinguish those theories with observational data.

### Withdrawal and actions that change a rule

Let $ d $ measure how far the actor is below the target,$ \mathcal A_T(d) $ be the actions still available before the deadline,$ c(d) $ be the cost of continuing, and $ V(d) $ be the value of using effort elsewhere. Define the best return from continued pursuit as

$$
M(d)=\max_{a\in\mathcal A_T(d)}
\{R_T(a;d)+B p_A(a;d)-c(d)\},
$$

where $ R_T $ excludes both the prize $ B $ and the continuation cost $ c(d) $. The actor withdraws when $ M(d)<V(d) $. The three-part pattern in the paper requires $ M(d)-V(d) $ eventually to fall as distance grows and to cross zero. Distance alone does not guarantee withdrawal: a remote target can still attract effort when the prize is large, a new action becomes available, or the outside option is poor.

For a local change in an action $ a $, allow the expected outcome $ \mu(a) $, spread $ \sigma(a) $, and target $ \theta(a) $ all to vary. Then

$$
\frac{d p_A}{d a}
=\frac{f(z)}{\sigma}
[\mu'(a)-\theta'(a)+z\sigma'(a)],
\qquad
z=\frac{\theta(a)-\mu(a)}{\sigma(a)}.
$$

The three terms describe changing the expected political outcome, changing the rule, and changing the spread of possible outcomes. With a fixed prize,$ dU_A/da=R_A'(a)+B\,dp_A/da $. If the action also changes the prize, the additional term is $ B'(a) p_A(a) $. This derivative describes small changes. Attempts to cancel certification or impose martial law are discrete actions and should not be read as numerical applications of Equation (rule-derivative).

## Additional Methods and Sensitivity Checks

### Coding procedure shared by the action studies

Three independent coders using OpenAI's GPT-5.6 Luna Max model classified the pre-action records with a fixed form. Each coder worked from the same evidence for a case. A field requires the agreement specified in its codebook; otherwise it remains unresolved. Individual coder records are available for both action studies.

The replication package contains the source records, evidence identifiers, available individual coder files, agreed labels, codebooks, and software-readable results. Agreement does not guarantee correct classification: the coders share a model family and may share its mistakes. OpenAI Codex agents assembled the action corpora by following the published protocols. The author checked the included cases and coding against the cited evidence.

##### Independent human validation.

Three anonymous human coders conducted a validation without seeing the existing labels. One coder checked each of 100 randomly selected episodes, split evenly between the countries. All 100 passed the actor, action, date, target, and distinct-episode checks; 99 had direct source support and one had partial support. Two coders independently recoded each of 40 cases, including 32 random and eight deliberately difficult cases. They agreed on all risk-taking and high-stakes labels, 97.5 percent of protection labels, 95.0 percent of withdrawal labels, and 92.5 percent of both accepted-sacrifice and position labels.

The model was more cautious about position: in eight random cases, both humans agreed on a definite position where the model left it unresolved. Holding the action codes fixed and using those positions left all six differences in the predicted direction. The German risk-taking difference changed from 12.6 to 11.8 percentage points ($ p=.042 $ to $ p=.049 $), and the U.S. difference changed from 14.6 to 12.7 points ($ p=.019 $ to $ p=.032 $); the other four differences changed by no more than 0.5 points. The replication files contain the anonymous responses and full results.

### German political actions

##### Collection and unit.

The documented German collection contains 500 cases from 20 study periods between 2005--06 and 2026. It covers municipal, district, state, federal, and European politics, including actions that span levels of government. Each case requires an identifiable actor, a dated action, an electoral or office target, a position before the action, evidence linking the action to the target, and a prior course or feasible alternative. The collection contains 276 actors, 432 actor--target groups, and 178 target decisions.

Evidence comes from original campaign material, official rules and results, public broadcasters, news agencies, polls, and established news reports. Each record preserves source links, dates, excerpts, archived files, and source limits. I store later evidence separately so it does not effect the pre-action record of the action, target, position, or classification.

##### Position.

Coders used only information available before the action. For a five-percent entry target, ``close'' means within three percentage points. For a two-sided contest, ``close'' means either a margin within ten points or a contemporary source describing the contest as close. I classify coalition, nomination, and office targets using seat calculations and public commitments. ``Far below'' means that the record shows no plausible route to the target before the relevant deadline, while ``far above'' means a secure position. I code a case as ``cannot determine'' when the evidence does not support any of these positions.

The final data contain 161 close-below, 72 close-above, 38 far-below, 10 far-above, and 14 at-target cases. Coders could not resolve the position in 205 cases, so I compare positions using the 295 cases for which coders resolved the position.

##### Action and stakes.

Risk taking requires both a new possible gain and a new possible loss. Protection requires an existing political advantage, a concrete threat, an action that blocks it, and an opportunity that the actor gives up. Withdrawal means that the actor stops pursuing the target. A separate form records whether the action puts policy value, reputation, resources, or average political support at risk or gives it up. Stakes concern the actor's office, career, entry into parliament, coalition or government survival, and future eligibility. I call stakes high when the record supports a high or exceptional personal consequence.

##### Inference and replication.

The main estimate is the difference between the two reported rates. For each comparison, I fit a linear probability model. Its one-sided p-value tests the direction predicted by the theory and accounts for repeated actions by the same actor and repeated observations of the same political target. The raw differences remain central. Checks that give each actor equal weight or omit one study period at a time do not change the broad pattern. Full results, including actor-only and target-only checks, are in the replication files.

### United States political actions

##### Collection and unit.

The documented U.S. collection contains 503 cases from the same 20 study periods, covering election-related actions at local, state, party, congressional, and presidential levels. Each record identifies the actor, action, date, target, pre-action position, evidence linking the action to the target, prior course or feasible alternative, and source limits. The collection contains 324 actors, 437 actor--target groups, and 271 target decisions.

##### Position, action, and tradeoffs.

The final data contain 49 close-below, 83 close-above, 63 far-below, 28 far-above, and 17 at-target cases; coders could not resolve the position in 263 cases. Polls, prior election results, seat or vote calculations, and contemporary descriptions determine the actor's position. Coders do not infer it from the action or final result.

The action definitions are the same in both countries. The U.S. form records whether pre-action evidence shows policy value, reputation, resources, or average political support put at risk or given up. It records costs visible before the action, not losses known only afterward. I call stakes high when the actor faces a high or exceptional personal consequence involving office, career survival, legislative entry, government survival, or future eligibility.

##### Inference and replication.

The U.S. analysis uses the same position comparisons and the same method as the German analysis. Full checks are in the replication files.

### Checks for the action studies

The checks below ask whether stakes and deadlines strengthen the three action differences, whether accepted sacrifice changes with pressure, and whether the German results depend on the kinds of targets in the sample. Both countries use all available cases.

> **Caption.** Do stakes and deadlines strengthen the action differences?

| *Panel A: High stakes compared with lower stakes* |  |  |  |  |
| --- | --- | --- | --- | --- |
| Country | Action pattern | High stakes | Lower stakes | Change |
| Germany | Risk taking | $+16.1 $ pp 64/89 vs. 24/43 | $+8.0 $ pp 48/72 vs. 17/29 | $+8.1 $ pp |
| Germany | Protection | $+2.3 $ pp 1/43 vs. 0/89 | $+3.4 $ pp 1/29 vs. 0/72 | $-1.1 $ pp |
| Germany | Withdrawal | $-10.5 $ pp 3/16 vs. 26/89 | $+39.3 $ pp 12/22 vs. 11/72 | $-49.7 $ pp |
| United States | Risk taking | $+17.8 $ pp 15/40 vs. 14/71 | $+2.8 $ pp 1/9 vs. 1/12 | $+15.0 $ pp |
| United States | Protection | $+19.7 $ pp 14/71 vs. 0/40 | $ 0.0 $ pp 0/12 vs. 0/9 | $+19.7 $ pp |
| United States | Withdrawal | $+71.4 $ pp 40/56 vs. 0/40 | $+42.9 $ pp 3/7 vs. 0/9 | $+28.6 $ pp |
| *Panel B: 30 days or less compared with more than 30 days* |  |  |  |  |
| Country | Action pattern | 30 days or less | More than 30 days | Change |
| Germany | Risk taking | $+10.1 $ pp 20/37 vs. 11/25 | $+11.2 $ pp 42/60 vs. 10/17 | $-1.1 $ pp |
| Germany | Protection | $+8.0 $ pp 2/25 vs. 0/37 | $ 0.0 $ pp 0/17 vs. 0/60 | $+8.0 $ pp |
| Germany | Withdrawal | $+47.7 $ pp 6/9 vs. 7/37 | $-23.3 $ pp 0/10 vs. 14/60 | $+71.1 $ pp |
| United States | Risk taking | $+12.8 $ pp 7/21 vs. 8/39 | $+17.4 $ pp 9/27 vs. 7/44 | $-4.6 $ pp |
| United States | Protection | $+7.7 $ pp 3/39 vs. 0/21 | $+25.0 $ pp 11/44 vs. 0/27 | $-17.3 $ pp |
| United States | Withdrawal | $+57.1 $ pp 8/14 vs. 0/21 | $+71.4 $ pp 35/49 vs. 0/27 | $-14.3 $ pp |

> **Caption.** Notes: Each cell in the two middle columns gives the position difference and then the counts for the positions in Table action-contrasts. In Panel A, ``Change'' subtracts the lower-stakes difference from the high-stakes difference. In Panel B, it subtracts the more-than-30-day difference from the 30-days-or-less difference.

> **Caption.** Accepted sacrifice across stakes and deadline cutoffs

*Panel A: Stake categories*

| Country | No listed personal stake | Moderate | High | Exceptional |
| --- | --- | --- | --- | --- |
| Germany | 103/129 (79.8%) | 57/144 (39.6%) | 137/191 (71.7%) | 23/35 (65.7%) |
| United States | 8/28 (28.6%) | 22/101 (21.8%) | 99/234 (42.3%) | 35/138 (25.4%) |

*Panel B: Shorter-deadline rate minus longer-deadline rate*

| Country | 14 days | 30 days | 60 days | 90 days | 120 days |
| --- | --- | --- | --- | --- | --- |
| Germany | $+2.5 $ pp | $-1.4 $ pp | $+4.1 $ pp | $+11.6 $ pp | $+18.0 $ pp |
| United States | $+1.7 $ pp | $+2.7 $ pp | $+6.6 $ pp | $+13.6 $ pp | $+12.2 $ pp |

> **Caption.** Notes: Accepted sacrifice means that the pre-action record shows policy value, reputation, resources, or average political support put at risk or given up. Panel B uses cases with exact deadlines. Unresolved sacrifice answers are omitted from the corresponding rates.

> **Caption.** German action comparisons by type of political target

| Action pattern | Type of target | Rate in first position | Rate in second position | Difference |
| --- | --- | --- | --- | --- |
| Risk taking | Proportional or legislative | 105/143 (73.4%) | 37/59 (62.7%) | $+10.7 $ pp |
|  | Direct local office | 5/12 (41.7%) | 1/9 (11.1%) | $+30.6 $ pp |
|  | Other | 2/6 (33.3%) | 3/4 (75.0%) | $-41.7 $ pp |
| Protection | Proportional or legislative | 1/59 (1.7%) | 0/143 (0.0%) | $+1.7 $ pp |
|  | Direct local office | 1/9 (11.1%) | 0/12 (0.0%) | $+11.1 $ pp |
|  | Other | 0/4 (0.0%) | 0/6 (0.0%) | $ 0.0 $ pp |
| Withdrawal | Proportional or legislative | 6/27 (22.2%) | 31/143 (21.7%) | $+0.5 $ pp |
|  | Direct local office | 7/7 (100.0%) | 4/12 (33.3%) | $+66.7 $ pp |
|  | Other | 2/4 (50.0%) | 2/6 (33.3%) | $+16.7 $ pp |

| Action pattern | Raw difference | Difference using the same mix of target types |
| --- | --- | --- |
| Risk taking | $+12.6 $ pp | $+10.3 $ pp |
| Protection | $+2.8 $ pp | $+2.5 $ pp |
| Withdrawal | $+16.5 $ pp | $+7.7 $ pp |

> **Caption.** Notes: The first and second positions match their order in Table action-contrasts. The second panel recalculates both positions using the same shares of the three target types.

The replication script verifies episode identifiers, source-file hashes, and the completeness of the coding files before producing the tables.

### U.S. Senate campaign appeals

##### Sample.

The source files contain 3,816 emails from 2022 and 4,523 from 2024. I keep candidate-authorized Senate messages and assign each the most recent forecast available before it. I then keep only the first occurrence of each candidate-specific template in the archive and exclude observations when the broad language measure or the forecast distance from zero, scaled by forecast uncertainty, is missing. The email-flow table reports the final sample.

##### Variables and main model.

For template $ j $, let $ m_j $ be the expected vote margin in the most recent earlier forecast,$ s_j $ the spread implied by that forecast's uncertainty interval, and $ t_j $ the number of days until the election. Define

$$
I_j=\mathbf 1(m_j<0),
q_j=\max\{-3,\min(m_j/s_j,3)\},
K_j=1-|q_j|/3.
$$

$ I_j $ equals one for a forecast underdog, and $ K_j $ is larger when the forecast is closer to an even race. The main model is

$$
\operatorname{logit}\Pr(Y_j=1)
=\alpha+\beta I_j+\gamma K_j+\lambda\log(1+t_j)
+\eta_{\text{incumbency}}+\pi_{\text{party}}+\tau_{\text{year}},
$$

where $ Y_j $ records whether the template describes the possibility of a large electoral gain. This is the broad language measure. The equation is a logistic regression for this yes-or-no outcome. I cluster standard errors by candidate campaign; a second estimate clusters them by Senate contest. The reported p-values are one-sided tests of the predicted positive underdog difference.

In the main model, the underdog coefficient is 0.840 with a campaign-clustered standard error of 0.272. The corresponding odds ratio is 2.32 (95 percent interval $[1.36,3.95]$,$ p=0.001 $).

> **Caption.** Email sample by election year

| Stage | 2022 | 2024 |
| --- | --- | --- |
| Observed candidate-authorized emails | 3,816 | 4,523 |
| First-use templates | 2,082 | 2,209 |
| Forecast leaders | 1,268 | 1,366 |
| Forecast underdogs | 814 | 843 |
| Candidate campaigns | 32 | 32 |
| Senate contests | 23 | 22 |

> **Caption.** Notes: Position uses the expected vote margin in the most recent earlier forecast. A negative margin identifies a forecast underdog and a positive margin a forecast leader; I use zero to label forecasts as ahead or behind, not as the legal 50-percent vote threshold. The two election years contain 45 distinct contests.

The broad language measure records whether a template describes the possibility of a large electoral gain. The analysis script applies a narrower exact-word check for terms such as*underdog*,*upset*, and*long shot*, and a separate check for routine fundraising language. The script and replication files document the full word lists and search rules.

Eighty-eight templates that meet the broad measure also contain one of the narrower terms. For this combined outcome, the underdog odds ratio is 6.30 (campaign-clustered 95 percent interval $[1.66,23.93]$,$ p=0.0034 $). The other 226 templates that meet the broad measure have an underdog odds ratio of 1.66 (95 percent interval $[0.90,3.07]$). This split describes wording within the broad outcome; it is not an independent test. A control for fundraising deadlines, goals, and dollar amounts also leaves the association similar: the underdog odds ratio is 2.30 (contest-clustered 95 percent interval $[1.46,3.64]$).

##### Alternative specifications.

A linear probability model reports effects in percentage points, and I cluster standard errors by contest. A weighted model gives each campaign equal total weight. An interaction between election year and underdog status tests whether the association changes in 2024. The interaction estimate is $-3.9 $ points with a standard error of 5.6 points, so the estimated association is not clearly different between the two years.

Local models use the signed standardized margin $ q_j $ and fit separate linear relationships on either side of zero. The local-email table reports estimates for alternative ranges around zero. The range is the largest absolute standardized margin that the model includes.

> **Caption.** Local email estimates at a zero expected margin

| Range around zero | Templates | Estimate | Standard error | $ p $-value |
| --- | --- | --- | --- | --- |
| 0.50 | 889 | $-0.001 $ | 0.019 | 0.515 |
| 1.00 | 2,380 | 0.027 | 0.012 | 0.010 |
| 1.96 | 3,765 | 0.005 | 0.025 | 0.424 |
| 3.00 | 4,291 | 0.022 | 0.018 | 0.114 |
| Quadratic, 3.00 | 4,291 | $-0.008 $ | 0.036 | 0.584 |

> **Caption.** Notes: Linear probability models include separate linear slopes in the signed margin on each side, election year, time to election, incumbency, and party. Standard errors cluster by Senate contest. The quadratic row also includes separate squared slopes.

##### Inference and replication.

The analysis script reports cluster-robust standard errors and a check that reverses the signs of scores after aggregating them within each group. The replication files document the full procedure and its seed.

The folder`email_study`contains the source extracts, script, and output tables. The script`email_study/scripts/analyze_submission_extensions.py`reproduces every email estimate in this section.

## Notes

[^1] By September, the ``autumn of reforms'' had grown into a full calendar: Merz promised a winter, a spring, a summer, and another autumn of reforms [@merz2025reforms].
[^2] Expected Utility Theory and Cumulative Prospect Theory yield similar predictions when the target is modeled as a kink in the utility function or a reference point.
[^3] Electoral campaigns are usually suspiciously quiet about their possible disadvantages. Thus, testing that second channel was not feasible.
