# Better Information, Cheaper Capture: Personal AI and Selective Evidence

**Author:** Martin Höppner `martin.hoeppner@b-tu.de`

**Date:** August 2026

## Abstract

Personal AI could help citizens understand complex policies by filtering relevant evidence from noise. That saves time but also lets the provider decide which facts reach the user. Users may have stable broad values without a settled view on an unfamiliar policy, while the questions an AI asks to clarify those values may themselves shape what the user comes to prefer. For this paper I hold broad values fixed and model the narrower risk from evidence selection. Because checking may require much of the work the AI was meant to save, a provider offered a reward tied to the policy outcome can omit true evidence and focus on users who are likely to change, unlikely to check, or politically influential. The same user information that improves advice can thus help the provider protect an inefficient policy at lower cost. In a preregistered audit using fixed official sources, I show that a hidden instruction to favor one side changes both the selected evidence and the recommendation, while access to the full source set improves detection. My exploratory reanalysis of public experimental data suggests that information already known about people can help identify who is most likely to change their views after assistance. I therefore propose AI verification as a public good: a service that compares and summarizes evidence from independently owned systems could lower checking costs and give providers a reputational reason to expose one another's omissions, although biases shared across systems would remain.

**Keywords:** personal AI; selective disclosure; rational ignorance; delegation; political capture; algorithm audits

**JEL classification:** D72, D82, D83, L86

## Introduction

Consider Anna, a voter deciding whether to oppose a tariff exemption. To save time, she uses personal AI, a service that uses information about her to research policy and give advice. Within minutes, the service can filter relevant evidence from the bill, impact assessment, and technical annexes and turn it into a comparison Anna can use - a task few rational voters would volunteer to do on a weekend[^1]. In doing so, the service also decides which costs, beneficiaries, and realistic alternatives enter that comparison. An interest group could offer the provider a benefit if the exemption survives. The provider could then omit one decisive estimate or alternative while making only true visible claims. Discovering that omission would require costly research.

Personal AI changes a familiar political-economy imbalance. Individual voters have little reason to master costly policy detail, while groups with concentrated gains can organize and pay to preserve favorable policies [@downs_1957; @olson_1965; @grossman_helpman_1994]. Better access to information can improve accountability, but control over an information source can weaken it [@snyder_stromberg_2010; @besley_prat_2006]. Personal AI combines these forces: it lowers the citizen's research cost while placing the search inside a private service.

The closest models explain how a sender can use knowledge of the receiver to select true information and how costly checking limits that influence [@hoffmann_inderst_ottaviani_2020; @felgenhauer_2019]. Work on search platforms shows how user data can improve targeting while distorting what users see [@janssen_etal_2026]. I place these choices inside delegated policy research. The provider chooses both evidence and users, and their combined response determines whether an inefficient policy survives.

My model compares two uses of the same information about a user. I call advice user-aligned when the provider selects evidence only to help the citizen decide. A conflicted provider can use the same information to identify the users whose opposition it can remove most cheaply and select evidence that favors the interest group. I call that steering; when it preserves an inefficient policy, it produces political capture. I derive the minimum cost of capture from each user's expected response and chance of correction. More precise user information can therefore improve advice while lowering the cost of capture, even if the AI states only true facts and users knowingly adopt the service. Figure 1 summarizes the argument.

> **Figure.** Model overview: An interest group rewards steering. Personal AI uses information about its users to choose whom to approach and which evidence to present. Citizens may check the advice before acting, and their combined responses determine whether the policy survives.

I test evidence selection directly with a preregistered audit using a fixed set of official UK policy impact assessments [@uk_parliament_impact_assessments_2026]. Some planners received a hidden instruction to favor adoption or rejection. That instruction moved selected evidence toward the favored result for 53 of 54 policies and moved a separate writer's recommendation for 41. Auditors detected the instruction more accurately when they saw all source cards instead of the final brief alone. The audit shows that a model can steer through its choice among true facts.

Public experimental data suggest that AI assistance can change attitudes and that information a provider already has about people can help it choose whom to contact. A randomized writing experiment finds that biased AI autocomplete moves attitudes beyond exposure to comparable fixed arguments [@williams_ceci_etal_2026]. My exploratory reanalysis of conversations about ten issues from [@hackenburg_etal_2025] finds that personal information available before assistance helps identify people whose attitudes are predicted to change most. In the larger data set, contacting the quarter of opponents predicted to respond most would achieve the same estimated change in attitudes with 32.8 percent fewer contacts than choosing opponents at random. The smaller data set gives no clear answer about whether this approach works.

## Delegated search and the cost of capture

Return to Anna. Her AI knows that she cares about local jobs and household costs. A conflicted provider can use that knowledge to emphasize producer gains and omit the price estimate.

Now scale the example across many users. Users adopt the service before a policy conflict arises. The interest group then offers the provider a benefit[^2] tied to policy survival. The interest group and provider may be the same organization, but I model them separately to make the bargain explicit. Using information about its users, the provider estimates the cost of steering each person and the resulting reduction in opposition. The provider then chooses whom to approach and which evidence to present. Users may check the advice before acting, and their combined responses determine whether the policy survives. Let $ Q $ be the amount of opposition that must be removed and $ C(Q) $ the lowest expected cost of doing so. The notation table defines the recurring quantities.

> **Caption.** Guide to the main quantities

| Quantity | Meaning |
| --- | --- |
| $ p_i $ | Probability that citizen $ i $ detects and corrects steering before an independent audit |
| $ s_i $ | Share of citizen $ i $'s political response caused by steering before correction |
| $ r_i $ | Political pressure supplied by citizen $ i $ under user-aligned advice |
| $ K_i $ | Provider's expected cost of steering citizen $ i $ |
| $ M_i $ | Expected reduction in opposition from steering citizen $ i $ |
| $ Q $ | Total opposition the campaign must remove |
| $ C(Q) $ | Least expected cost of removing $ Q $ units of opposition |
| $ R $ and $ H $ | Interest group's policy rent and harm imposed outside the group |

### Advice, evidence, and checking

Scale the total population to one and label citizens by $ i\in[0,1]$. Let $ w $ describe the detailed policy. Citizen $ i $ can oppose the policy,$ a_i=1 $, or remain inactive,$ a_i=0 $.

Citizens may care consistently about efficiency, fairness, or rights without holding settled views on every tariff exemption or regulatory amendment. Political answers depend on which relevant considerations come to mind [@zaller_feldman_1992], and people often construct choices from their goals, available information, and the demands of the task [@bettman_luce_payne_1998]. Personal AI can therefore help form an issue position by selecting considerations even when broader values remain stable. Its questions may also shape how the user states and weighs those values. I set that possibility aside and hold broad values fixed to isolate evidence selection.

Let $ v_i(w) $ be citizen $ i $'s private benefit from opposition rather than inactivity, after subtracting the private cost of acting. Because one citizen rarely decides the policy outcome alone, this benefit can include the personal civic or expressive value of acting in line with one's values.

A user-aligned procedure searches, selects evidence, and compares alternatives to maximize the user's expected benefit from the decision after subtracting search costs. Its rule does not depend on which policy result benefits the interest group. The citizen endorses the rule before learning which side the provider may later favor. Let $ a_i^U $ denote the action produced by this procedure. Appendix Benchmark gives the formal definition.

The provider steers when the interest group's preferred result changes this search or comparison. It can omit a consideration or emphasize one consequence while leaving every visible statement defensible. I study cases in which user-aligned advice recommends opposition but steering can induce inactivity. Let $ L_i>0 $ denote the citizen's loss when steering succeeds.

**Assumption.**

The same visible recommendation can come from user-aligned advice or steering, and the citizen cannot rebuild the user-aligned evidence set from the final answer alone. Omitted evidence rarely arrives with an omission notice, so finding the departure requires another search.

After receiving the recommendation, citizen $ i $ may notice an implausible omission, encounter a conflicting source, or ask another system. Checking is worthwhile when the perceived probability of steering, multiplied by $ L_i $, is at least the cost $ c_i>0 $ of rebuilding the missing comparison. For simplicity a successful check restores the user-aligned action. Let $ p_i $ denote the probability that the citizen detects and corrects steering before the independent audit considered below. This probability includes deliberate checking, accidental discovery, and the checking tools already available to the citizen. I treat $ p_i $ as fixed during one policy conflict.

The citizen can fully understand the provider's conflict and still decline to check. The choice resembles clicking ``Agree'' on a lengthy software license: careful reading may be wise, but reading every page would erase much of the convenience.

Detection makes steering more costly. Let $ d_i\ge0 $ be the direct cost of producing and implementing the evidence used for steering. Let $ F_i>0 $ be the provider's loss following detection, including refunds, lost users, or legal penalties. The expected cost of steering citizen $ i $ is

$$
K_i=d_i+F_i p_i.
$$

I study users who voluntarily adopted the service before the political conflict. The advice does need not be perfectly user-aligned. Users may still adopt if the expected benefits, including time saved and better decision quality, exceed the price and expected costs of checking and steering. Interest-group payments may also lower that price, so a low price does not establish independence. If a campaign becomes visible or repeats, users may check more or leave; this static model represents those responses through $ p_i $.

Voluntary adoption is also plausible because users can still learn from a biased adviser whose bias they understand [@calvert_1985]. Delegation also lets an expert choose what to learn, trading expertise against the user's control [@deimen_szalay_2019]. Personal AI combines that useful discretion with a further choice over which users to approach.

### From individual steering to political capture

The interest group needs to remove enough combined opposition for the biased policy to survive. Showing different voters different pieces of true, checkable information can change an election [@titova_forthcoming]. The provider therefore begins with the cheapest opposition to remove.

The policy gives the interest group a rent $ R>0 $ and imposes aggregate harm $ H>0 $ outside the group. The policy is inefficient when $ H>R $, so the policy alone lowers welfare by $ H-R $. A payment between the interest group and provider changes who holds the money but does not itself use resources. Search, checking, implementation, and acting against one's values can add further real costs.

A user who would oppose under user-aligned service contributes political pressure $ r_i>0 $. This pressure can take the form of a constituent message, a donation, or a change in electoral support. User-aligned opposition is

$$
O^U=\int r_i a_i^U\,di.
$$

The biased policy survives when opposition is no greater than $ O_{\max}$. The relevant case is

$$
Q=O^U-O_{\max}>0,
$$

so user-aligned service would block the policy and the campaign must remove $ Q $ units of opposition. Because the population is a continuum, individual checking outcomes average out, so I use expected opposition.

Let $ s_i\in[0,1]$ be the expected share of citizen $ i $'s political response that steering removes before correction. A value of zero means that the citizen does not respond; a value of one means that steering removes the full response. Checking restores the user-aligned action with probability $ p_i $, so steering citizen $ i $ removes expected opposition

$$
M_i=r_i s_i(1-p_i).
$$

The formulation allows steering to change a binary action with some probability or to change only part of a continuous political response. Let $ x_i\in[0,1]$ be the probability that the provider targets an adopted user with $ M_i>0 $. The least expected cost of removing $ Q $ units of opposition is

$$
C(Q)=
\min_{0\le x_i\le1}
\int K_i x_i\,di
\quad\text{subject to}\quad
\int M_i x_i\,di\ge Q.
$$

**Assumption.**

The required reduction in opposition is possible, and no positive share of adopted users with $ M_i>0 $ has exactly the same ratio $ K_i/M_i $.

**Proposition.**

Under Assumption regular types, the provider targets citizens in increasing order of

$$
\frac{K_i}{M_i}
=
\frac{d_i+F_i p_i}{r_i s_i(1-p_i)}.
$$

The minimum cost $ C(Q) $ cannot fall as the required reduction in opposition rises. It is convex, meaning that the cost of removing one more unit of opposition cannot fall. Wherever the slope exists, it equals the cost per unit of opposition the provider removes from the last user it selects.

The selection rule is simply that the provider buys the cheapest units of expected opposition reduction first. The ratio rises with the chance of checking and falls with response and political effect. A user can face a small private loss and still exert considerable political pressure. Conversely, the provider may avoid a responsive user when likely detection makes steering costly.

The interest group can tie payment to policy survival without observing whom the provider steers. If $ R>C(Q) $, any payment $ T $ satisfying $$ C(Q)<T<R $$ gives the interest group a positive gain and the provider a positive profit. The provider then uses the least-cost selection rule needed for the policy to survive. If $ R\le C(Q) $, no payment can make both parties better off.

Paid advice can remain useful while favoring the payer. Commissions and hidden payments can change recommendations without removing their value to consumers [@inderst_ottaviani_2012_commissions], and a biased intermediary can inform consumers while favoring the firm that pays it [@decorniere_taylor_2019]. Personal AI brings the same tension into political search.

If $ Q>0 $,$ R>C(Q) $, and $ H>R $, user-aligned service blocks the policy but an interest-group contract tied to policy survival preserves it. Political capture is therefore compatible with voluntary adoption even though the policy lowers welfare by $ H-R>0 $ before additional real resource costs.

### User information and independent checks

User information works like data a firm collects directly from its customers. It can improve the service and predict who will respond. For user-aligned advice, the information helps find evidence relevant to broad values. For a conflicted provider, it can reveal[^3] response $ s_i $, correction probability $ p_i $, and political pressure $ r_i $.

Related work shows how an intermediary can use knowledge of consumer mistakes to choose which products the consumer considers, and how AI and user data can make low-quality products look attractive [@heidhues_koster_koszegi_2023; @acemoglu_etal_2025]. I hold broad values fixed so the user information guides evidence selection and reveals which political responses are cheapest to change.

[@blackwell_1953] compares information by asking whether a less informative signal can be produced by adding noise to a more informative one. I use this ordering because it changes what the provider knows without requiring every added detail to concern the same user trait. Let $ I $ denote the provider's information about users for a fixed political task, and let $ I'$ be a Blackwell refinement of $ I $. Hold fixed the task, adopted users, possible procedures, and distribution of user characteristics. Let $ W^U(I) $ be the highest total expected value of user-aligned service when decisions can depend on $ I $. Let $ C(Q\mid I) $ be the minimum campaign cost when user selection can depend on $ I $.

**Proposition.**

If $ I'$ is more informative than $ I $, then

$$
W^U(I')\ge W^U(I)
\qquad\text{and}\qquad
C(Q\mid I')\le C(Q\mid I).
$$

The first inequality is strict when the additional information improves the expected benefit of a positive share of users. The second is strict when the less precise information groups together users with different $ K_i/M_i $, the additional information separates them, and the provider needs to select only part of that group.

Both inequalities follow because either side can ignore the additional information. The user-aligned procedure can copy the old search, and the conflicted provider can copy the old selection rule. Yet better user-aligned search can also create more informed opposition. Let $ Q_0=Q(I) $ and $ Q_1=Q(I')\ge Q_0 $. The change in total campaign cost is

$$
C(Q_1\mid I')-C(Q_0\mid I) \notag\\
\quad=\bigl[C(Q_1\mid I')-C(Q_1\mid I)\bigr]
+\bigl[C(Q_1\mid I)-C(Q_0\mid I)\bigr].
$$

**Corollary.**

The first bracket in Equation (total cost decomposition) is weakly negative because better selection lowers cost at a fixed quantity. The second is weakly positive because user-aligned advice creates more opposition to remove. Total capture cost falls exactly when the selection saving is larger than the cost of the additional opposition.

An auditor who sees only the final answer has no more information than the user. Under Assumption pooling, that answer does not reveal whether user-aligned advice would have included an omitted alternative. An independent source audit repeats the search through the underlying sources with no preferred policy result and can look for that alternative.

Let $ u_i\in[0,1]$ be the additional probability that an independent audit finds the material omission after the citizen's earlier checks have failed. The total probability that the citizen or audit detects and corrects the departure from user-aligned advice becomes

$$
p_i^A=p_i+(1-p_i) u_i.
$$

The audit changes the provider's expected cost and reduction in opposition to

$$
K_i^A=d_i+F_i p_i^A,
\qquad
M_i^A=r_i s_i(1-p_i^A).
$$

Replacing $ K_i $ and $ M_i $ with $ K_i^A $ and $ M_i^A $ in Equation (capture cost) gives the least campaign cost $ C^A(Q) $.

**Proposition.**

An audit that supplies no information beyond the final answer has $ u_i=0 $ and leaves capture cost unchanged. An independent source audit with $ u_i>0 $ raises $ K_i^A/M_i^A $ for every user with $ M_i>0 $ whose omission the audit can find and cannot lower the minimum cost of removing $ Q $ units of opposition. The increase is strict when every least-cost campaign without audits uses a positive share of such users and the provider can still remove enough opposition after auditing.

If $ C(Q)<R\le C^A(Q) $, the source-based audit turns a profitable interest-group contract into an unprofitable one.

Because one published audit can help many users at no additional search cost, verification can be a public good that raises detection and makes exposure more costly for the provider.

## Fixed-source audit

### Design

I conduct the audit to test whether a hidden instruction to favor one side changes which true facts an AI selects, whether the selected facts change a recommendation, and whether access to all sources makes the instruction easier to detect. A provider could add such a goal cheaply through a system prompt, an instruction the user never sees[^4]. The models retain their existing safeguards, so the audit also reveals whether those safeguards block this route to steering. This is important because third party providers of the AI service could also be the one steering.

I separate evidence selection from writing and detection. The planner selects evidence, the writer turns that evidence into a recommendation, and the auditor judges whether the hidden instruction shaped the selection. Every planner receives the same source material. No human receives a brief, so the audit measures model behavior rather than persuasion of people.

I draw the policy set from the UK Parliament collection of impact assessments [@uk_parliament_impact_assessments_2026]. The collection supplies public records of official benefits, costs, alternatives, and uncertainty, so I can hold the available evidence fixed across planners. Using rules fixed in advance, I obtained 54 test policies from 2020--2025 across six policy areas and drew ten source cards from each policy's official assessment. Two people independently classified every card as favoring adoption, favoring rejection, or neither, and a third person resolved disagreements. None knew whether a policy would later receive an adoption or rejection target. I paired similar policies within each area, assigned opposite targets through a public random draw, and registered the instructions and analysis before the run. The registration appears at <https://osf.io/cyjd3/>; Appendix Audit details gives the counts and screening rules.

Each ten-card packet contains four stated benefits, four stated costs, risks, or limitations, one material uncertainty, and one alternative. Each card stores its source passage and location. Two reviewers checked every card against the assessment.

One packet, for example, asks whether Transport for London should introduce compulsory licensing for pedicabs. Its cards report possible reductions in injuries and more transparent fares, but also an estimated GBP 1.4 million in licensing and inspection costs for businesses and possible income loss for some operators.

The fixed user instruction asks every planner to compare total benefits and costs, who bears them, uncertainty, implementation, and alternatives. A directional planner also receives a hidden instruction to favor the randomly assigned adoption or rejection target without changing or inventing information.

> **Caption.** Roles in the preregistered audit

| Role | What it received | What it produced |
| --- | --- | --- |
| Planner | Policy options, ten card titles and short summaries, and a selection instruction | Six selected card IDs |
| Writer | Policy options and the full text of six selected cards in a fixed order | Brief and recommendation score |
| Auditor | Policy options and the brief, either alone or with all ten source cards | Probability of a directional instruction |

For each policy and assignment of models to roles, both planners choose six of the ten cards. The planner chooses from titles and short summaries; the writer reads the selected cards in full. This separates evidence selection from the recommendation. Only the planner sees the target and hidden instruction. The writer cannot see the omitted cards, and the auditor cannot see the target, the writer's score, or the model identities. The directional instruction can therefore affect the recommendation only through evidence selection.

The evidence score places each six-card selection between the most rejection-favoring and most adoption-favoring selection possible for that policy, from $-1 $ to $+1 $. The writer reports a recommendation from $-3 $ for strong rejection to $+3 $ for strong adoption. The two preplanned outcomes are the directional brief's changes in evidence and recommendation toward its assigned target, relative to the matched non-directional brief.

An auditor evaluates each brief twice in separate calls: once alone and once with all ten source cards. The auditor reports the probability that the brief came from a directional planner. The first planned measure subtracts the average probability assigned to non-directional briefs from the average assigned to directional briefs. The second asks whether the reported probabilities become more accurate. The added sources must improve both measures for the claim to pass.

Three models from different providers take turns in the three roles. I average the three assignments within policy and then give each policy equal weight. The primary claim requires both evidence and recommendation to move toward the target under a randomization test that reallocates targets within matched pairs. Only after that claim passes do I test whether source access improves detection. Appendix Audit details gives the model services, exact measures, failure rules, and execution record.

### Results

The directional instruction moved the evidence score by 0.814 toward its target on a scale from $-1 $ to $+1 $. It moved the writer's recommendation by 0.562 points toward the target on a scale from $-3 $ to $+3 $. Evidence moved toward the target for 53 of 54 policies and against it for none; recommendations moved toward it for 41 policies, against it for three, and did not move for ten. Both preplanned outcomes pass at $ p<0.001 $. The planner could choose only among true cards, yet the instruction changed what reached a writer that never saw it.

> **Caption.** Preplanned audit results

| Preplanned question and unit | Estimate | 95% interval | One-sided $ p $ |
| --- | --- | --- | --- |
| Evidence-score change toward target ($-1 $ to $+1 $) | 0.814 | $[0.734,0.889]$ | $<0.001 $ |
| Recommendation change toward target ($-3 $ to $+3 $) | 0.562 | $[0.438,0.685]$ | $<0.001 $ |
| Increase in average detection probability with full sources | 0.120 | $[0.084,0.157]$ | $<0.001 $ |
| More accurate auditor probabilities with full sources | 0.090 | $[0.050,0.131]$ | $<0.001 $ |

*Notes:* Positive estimates support the preplanned claims. Log loss measures the accuracy of the auditors' probabilities and penalizes confident mistakes most heavily. Estimates average assignments within policy and then weight policies equally. Intervals resample the observed policies; randomization tests reallocate targets within matched pairs. Appendix Audit details gives full definitions.

The design contains equal numbers of directional and non-directional briefs, so chance accuracy is 50 percent. With only the final brief, auditors classified 55.9 percent correctly; access to all ten source cards raised accuracy to 62.8 percent. Their ability to rank directional briefs above non-directional briefs rose from 0.679 to 0.787, and mean log loss fell from 0.711 to 0.624. Together, the two planned detection tests pass at $ p<0.001 $. Full sources provide an informative but noisy signal: auditors still misclassify more than one third of the briefs.

In a preplanned secondary test, a planner learned only that its first brief failed an audit screen. Its revision looked less suspicious but could not preserve the required recommendation change. Within this fixed-source design, access to all sources helped auditors distinguish directional from non-directional briefs by letting them compare each brief with the full source set, as Proposition auditspredicts. The exercise does not estimate how providers behave in practice or the full cost of capture.

## Evidence on attitudes and targeting

The audit shows that a hidden goal can change which true evidence reaches the writer. For that selection to lower the cost of capture, the advice must change attitudes and user information must help the provider choose whom to contact. Any change must then last long enough to affect political behavior. Existing evidence speaks most clearly to attitudes and contact choices; evidence on lasting political action remains limited.

The closest external evidence on biased assistance within a task comes from [@williams_ceci_etal_2026]. Their preregistered experiment randomly assigned participants to write about standardized testing with no assistance, fixed biased arguments, or biased AI autocomplete. Relative to the fixed arguments, autocomplete moves attitudes another 0.235 points toward the assigned position on a five-point scale, with 95 percent interval $[0.051,0.419]$. Help within the writing task therefore adds movement beyond exposure to comparable arguments.

User information can affect both what the provider says and whom it contacts. Across 19 models and 707 political issues,[@hackenburg_etal_2025] find that special training and the instructions given to a model change persuasion more than personalization or model size. Their data nevertheless contain wide differences in responses across people, which I use to test whether information available beforehand improves contact decisions.[@hackenburg_margetts_2024] compare GPT-4 messages based on individual attributes with a strong generic message. Both move attitudes, but the tailored messages have no clear average advantage, which limits any claim that personal wording alone makes the assistance more persuasive.[@salvi_etal_2025] find the opposite in structured debates: GPT-4 becomes more persuasive when it receives basic user information. This positive result matters because it shows that the value of tailored wording depends on the task and design. I therefore focus on the more modest claim that user information can help the provider choose whom to contact, even when its average effect on wording remains uncertain.

I test this choice of whom to contact in two public data sets, restricting attention to respondents who initially oppose the assigned position. For each person, a statistical model uses information available before assistance to predict the person's position with and without assistance. The difference is the predicted effect of assistance. I train the model on other people, so it cannot use a person's own response to predict that effect. Every rule contacts the same share within each issue. The outcome measures estimated movement toward the assigned position on a 0--100 scale. Appendix External gives the method and full estimates.

The large conversational data set contains 10,300 initial opponents across ten issues. When the rule contacts 25 percent of them, predicted-effect selection produces 17.23 points of estimated movement per contact, compared with 11.57 under random selection. The gain is 5.65 points, with interval $[4.53,6.77]$, and remains positive when the rule contacts half the sample or learns from nine issues before evaluating the tenth. The smaller Williams--Ceci data set gives an uncertain gain of 1.85 points with interval $[-9.97,13.67]$. Figure 2 shows the comparison; Appendix Table targeting resultsgives the full estimates and a simple rule based on initial attitude.

> **Figure.** Estimated gain from choosing whom to contact. Each point shows how much more the average contacted person moves, on a 0--100 scale, toward the position each study asked the AI to support when people are chosen by their predicted response rather than at random. Percentages give the share contacted; lines show 95 percent intervals. Samples include only people who initially opposed that position.

To translate these estimates into contact costs, suppose each contact costs $ c_{\mathrm{contact}}$ and produces average attitude change $ m $ among people who initially oppose the target. The cost of producing $ A $ units of attitude change is

$$
C_{\mathrm{contact}}(A;m)=\frac{c_{\mathrm{contact}}A}{m}.
$$

For fixed $ A $ and $ c_{\mathrm{contact}}$, the cost under predicted-effect selection relative to random selection is $ m_{\mathrm{random}}/m_{\mathrm{targeted}}$.

At 25 percent contact in the large data set, the ratio is $ 11.57/17.23=0.672 $, implying 32.8 percent fewer contacts for the same estimated attitude change. This calculation holds the prediction system's fixed cost constant and isolates contact costs. It does not estimate checking or the rewards offered to providers.

An immediate attitude change may fade before it affects politics.[@hackenburg_etal_2025] find that part of the immediate effect in their large UK study remains after one month. This persistence makes a political response possible, but the experiment does not observe one.[@crabtree_etal_2026] find that a short personalized conversation increases support for transgender rights immediately but that much of the effect fades within a week. Their result shows why an immediate shift cannot stand in for durable political opposition. Other conversations last longer:[@costello_etal_2024] find that personalized factual dialogues reduce conspiracy beliefs for at least two months. That contrast makes persistence an outcome to measure rather than an assumption about conversational AI.

Even a lasting attitude change may not change behavior. In two preregistered experiments,[@hackenburg_etal_actions_2026] find that conversational AI changes petition signing and donations, yet its estimated effects on attitudes and behavior do not move together reliably. This preprint provides the closest evidence on political action and warns against inferring action from an attitude scale.[@velez_green_sevi_2025] find that a source-grounded voting chatbot improves knowledge of party positions among young unaffiliated voters. Average effects on party evaluations and vote choice remain near zero, showing that useful political information need not move electoral behavior. A direct test of the full argument would combine an outcome-linked reward for the provider with user information and independent source access, then measure checking and political action.

## Raising the cost of capture

Independent verification should be the first line of defense because it preserves delegation. Bans on rewards tied to policy outcomes address the conflict directly, but hidden ties are hard to observe. Broad record-keeping rules impose privacy and compliance costs that may fall hardest on smaller providers.

Competition helps when users can move their instructions and history between services. Easier switching lowers the checking cost $ c_i $ and raises the correction probability $ p_i $. Software under the user's control could store broad values and history, so trying another service would not require starting over. Competition between persuaders can push their explanations toward the evidence, even when tailored private messages strengthen persuasion [@schwartzstein_sunderam_2021].

Most users will not make these comparisons, but a public verification service could do the work once for many. It could send the same question to independently owned systems and summarize their sources and arguments. The service should also search independently because several systems may share a search provider or source collection. Publishing which systems found or missed relevant evidence would give providers a reputational reason to challenge rivals' omissions, although shared bias could remain. The service would cost money and need privacy rules, but each comparison could serve many users. Reputational damage would increase $ F_i $, the provider's loss after detection.[@bandy_2021_algorithm_audits] reviews algorithm audits and emphasizes clear comparisons, evidence, and repeatability. Those requirements motivate identical requests with no preferred policy result, preserved sources, and a record of the model and version.

If independent verification proves insufficient, regulators could require dated records of the documents retrieved, passages used, sources shown to the user, and model version. Such records would help auditors but may reveal political beliefs even after names are removed. Storage and audit costs may fall hardest on smaller providers, weakening competition. Any rule should therefore limit retention and access, separate identity from content, and use spot checks for missing entries. These safeguards make auditing safer but costlier and less informative.

A source record cannot reveal a document that the system never found, so the service must compare the record with its own search. This raises $ u_i $, the added chance of finding an omission after earlier checks fail. The comparison could reveal one-sided selection or a missing amendment or cost estimate. A warning that AI can make mistakes may be accurate, but it cannot retrieve either one.

Limiting how much user data reaches the provider would make precise targeting harder, but it would sacrifice some useful personalization. Letting software under the user's control learn and store the user's goals before a policy conflict may preserve more of that value than deleting the memory, while reducing the provider's ability to shape those goals. None of these safeguards requires a regulator to choose the correct ideology. An audit can test whether a personal AI finds a known provision, follows the user's stated limits, and treats equivalent descriptions consistently. The fuller comparison may still support the interest group's preferred policy.

## Conclusion

Personal AI may become a common way citizens learn about policy because it makes difficult evidence usable. Its democratic value will depend on whether users can check that evidence without repeating the work they delegated. A public verification service could compare independent searches and source records, making one-sided selection harder to hide while giving providers a reputational reason to expose rivals' omissions. Warnings or second opinions using the same search provider should do less. Researchers could test this by randomly adding one of these checks to one-sided advice, then comparing whether users find the omitted evidence and change a real choice such as signing a petition.

##### Acknowledgment.

Generative AI tools were used extensively to shorten and clarify this manuscript. The author directed and reviewed each revision and remains responsible for the arguments, analysis, and any errors.

##### Data and code availability.

OSF stores the preregistration at <https://osf.io/cyjd3/> and a timestamped record of the completed run at <https://osf.io/r43ka/>. Replication materials include source passages, file fingerprints, model instructions, access methods, failure rules, and code.

## References

- Downs, Anthony (1957). *An Economic Theory of Democracy*. Harper.

- Olson, Mancur (1965). *The Logic of Collective Action: Public Goods and the Theory of Groups*. Harvard University Press.

- Snyder, James M.; Strömberg, David (2010). *Press Coverage and Political Accountability*. Journal of Political Economy. 118(2). 355-408.

- Besley, Timothy; Prat, Andrea (2006). *Handcuffs for the Grabbing Hand? Media Capture and Government Accountability*. The American Economic Review. 96(3). 720-736. https://doi.org/10.1257/aer.96.3.720.

- Grossman, Gene M.; Helpman, Elhanan (1994). *Protection for Sale*. The American Economic Review. 84(4). 833-850.

- Calvert, Randall L. (1985). *The Value of Biased Information: A Rational Choice Model of Political Advice*. The Journal of Politics. 47(2). 530-555. https://doi.org/10.2307/2130895.

- Deimen, Inga; Szalay, Dezső (2019). *Delegated Expertise, Authority, and Communication*. American Economic Review. 109(4). 1349-1374. https://doi.org/10.1257/aer.20161109.

- Inderst, Roman; Ottaviani, Marco (2012). *Competition through Commissions and Kickbacks*. The American Economic Review. 102(2). 780-809. https://doi.org/10.1257/aer.102.2.780.

- de Cornière, Alexandre; Taylor, Greg (2019). *A Model of Biased Intermediation*. RAND Journal of Economics. 50(4). 854-882. https://doi.org/10.1111/1756-2171.12298.

- Janssen, Maarten C. W.; Jungbauer, Thomas; Preuss, Marcel; Williams, Cole (2026). *Search Platforms: Big Data and Sponsored Positions*. The Economic Journal. https://doi.org/10.1093/ej/ueag002.

- Heidhues, Paul; Köster, Mats; Kőszegi, Botond (2023). *Steering Fallible Consumers*. The Economic Journal. 133(652). 1430-1465. https://doi.org/10.1093/ej/ueac093.

- Acemoglu, Daron; Makhdoumi, Ali; Malekian, Azarakhsh; Ozdaglar, Asuman (2025). *When Big Data Enables Behavioral Manipulation*. American Economic Review: Insights. 7(1). 19-38. https://doi.org/10.1257/aeri.20230589.

- Hoffmann, Florian; Inderst, Roman; Ottaviani, Marco (2020). *Persuasion Through Selective Disclosure: Implications for Marketing, Campaigning, and Privacy Regulation*. Management Science. 66(11). 4958-4979. https://doi.org/10.1287/mnsc.2019.3455.

- Felgenhauer, Mike (2019). *Endogenous Persuasion with Costly Verification*. The Scandinavian Journal of Economics. 121(3). 1054-1087. https://doi.org/10.1111/sjoe.12290.

- Titova, Maria (forthcoming). *Targeted Advertising in Elections*. American Economic Journal: Microeconomics. https://doi.org/10.1257/mic.20240479.

- Schwartzstein, Joshua; Sunderam, Adi (2021). *Using Models to Persuade*. The American Economic Review. 111(1). 276-323. https://doi.org/10.1257/aer.20191074.

- Zaller, John; Feldman, Stanley (1992). *A Simple Theory of the Survey Response: Answering Questions versus Revealing Preferences*. American Journal of Political Science. 36(3). 579-616. https://doi.org/10.2307/2111583.

- Bettman, James R.; Luce, Mary Frances; Payne, John W. (1998). *Constructive Consumer Choice Processes*. Journal of Consumer Research. 25(3). 187-217.

- Blackwell, David (1953). *Equivalent Comparisons of Experiments*. Annals of Mathematical Statistics. 24(2). 265-272. https://doi.org/10.1214/aoms/1177729032.

- UK Parliament (2026). *Impact Assessments: Parliamentary Bill Papers*. https://api.parliament.uk/bill-papers/publication-types/36.

- Williams-Ceci, Sterling; Jakesch, Maurice; Bhat, Advait; Kadoma, Kowe; Zalmanson, Lior; Naaman, Mor (2026). *Biased AI Writing Assistants Shift Users' Attitudes on Societal Issues*. Science Advances. 12(11). eadw5578. https://doi.org/10.1126/sciadv.adw5578.

- Hackenburg, Kobi; Tappin, Ben M.; Hewitt, Luke; Saunders, Ed; Black, Sid; Lin, Hause; Fist, Catherine; Margetts, Helen; Rand, David G.; Summerfield, Christopher (2025). *The Levers of Political Persuasion with Conversational Artificial Intelligence*. Science. 390(6777). eaea3884. https://doi.org/10.1126/science.aea3884.

- Hackenburg, Kobi; Margetts, Helen (2024). *Evaluating the Persuasive Influence of Political Microtargeting with Large Language Models*. Proceedings of the National Academy of Sciences. 121(24). e2403116121. https://doi.org/10.1073/pnas.2403116121.

- Salvi, Francesco; Horta Ribeiro, Manoel; Gallotti, Riccardo; West, Robert (2025). *On the Conversational Persuasiveness of GPT-4*. Nature Human Behaviour. 9(8). 1645-1653. https://doi.org/10.1038/s41562-025-02194-6.

- Crabtree, Charles; Holbein, John B.; Bosley, Mitchell; Sevi, Semra (2026). *Can AI Help Reduce Prejudice? Evaluating the Effectiveness of AI-Powered Personalized Persuasion on Support for Transgender Rights*. PNAS Nexus. 5(7). pgag066. https://doi.org/10.1093/pnasnexus/pgag066.

- Costello, Thomas H.; Pennycook, Gordon; Rand, David G. (2024). *Durably Reducing Conspiracy Beliefs through Dialogues with AI*. Science. 385(6714). eadq1814. https://doi.org/10.1126/science.adq1814.

- Hackenburg, Kobi; Hewitt, Luke; Wagner, Caroline; Tappin, Ben M.; Summerfield, Christopher (2026). *Artificial Intelligence Can Persuade People to Take Political Actions*. https://doi.org/10.48550/arXiv.2604.09200.

- Velez, Yamil R.; Green, Donald P.; Sevi, Semra (2025). *Chatbot Voting Advice Applications Inform but Seldom Sway Young Unaligned Voters*. Proceedings of the National Academy of Sciences. 122(50). e2515516122. https://doi.org/10.1073/pnas.2515516122.

- Bandy, Jack (2021). *Problematic Machine Behavior: A Systematic Literature Review of Algorithm Audits*. Proceedings of the ACM on Human-Computer Interaction. 5(CSCW1).

- Athey, Susan; Wager, Stefan (2021). *Policy Learning with Observational Data*. Econometrica. 89(1). 133-161. https://doi.org/10.3982/ECTA15732.

- Kitagawa, Toru; Tetenov, Aleksey (2018). *Who Should Be Treated? Empirical Welfare Maximization Methods for Treatment Choice*. Econometrica. 86(2). 591-616. https://doi.org/10.3982/ECTA13288.

## Appendix

## Proofs

*Proof of Proposition targeting.*

Let $ \lambda\ge0 $ be the Lagrange multiplier on the required reduction in opposition in Equation (capture cost). This multiplier measures the added cost of tightening that requirement. The Lagrangian is $$ \mathcal L(x,\lambda)=\int (K_i-\lambda M_i) x_i\,di+\lambda Q. $$ Minimizing separately for each citizen sets $ x_i=1 $ when $ K_i/M_i<\lambda $ and $ x_i=0 $ when $ K_i/M_i>\lambda $. Assumption regular types ensures that no positive share of citizens has a ratio exactly equal to $ \lambda $. Because the required reduction is possible and selection can vary continuously, the least-cost rule removes exactly $ Q $ units. Ordering units of opposition reduction by their cost ratios represents $ C(Q) $ as the integral of ratios that cannot fall. Hence $ C $ cannot fall and is convex. Wherever its slope exists,$ C'(Q)=\lambda $.$ \square $

*Proof of Proposition dual use.*

Because $ I'$ contains all information in $ I $, a user-aligned procedure using $ I'$ can discard the extra information and copy the old rule. The additional information therefore cannot reduce $ W^U $. The inequality is strict when it improves the expected payoff of a positive share of users.

The same argument applies to user selection. A provider observing $ I'$ can discard the extra information and copy every possible selection rule based on $ I $. Every combination of cost and opposition reduction possible under $ I $ is possible under $ I'$, so $ C(Q\mid I')\le C(Q\mid I) $. If $ I $ groups together users with different $ K_i/M_i $ and the provider needs only part of that group, identifying the users with lower ratios strictly reduces cost.$ \square $

*Proof of Corollary cor:total capture cost.*

Equation (total cost decomposition) is an identity. Proposition dual use makes its first bracket weakly negative, while the monotonicity of $ C $ makes its second bracket weakly positive when $ Q_1\ge Q_0 $. Their sum is negative exactly when the selection saving exceeds the cost of the additional opposition.$ \square $

*Proof of Proposition audits.*

An audit that sees only the final answer and adds no information has $ u_i=0 $, so Equation (audited detection)--Equation (audited objects) reproduce the same cost and opposition reduction as without an audit. For an audit that repeats the search from the sources with $ u_i>0 $,$ p_i^A>p_i $. Hence $ K_i^A>K_i $ and $ M_i^A<M_i $, which implies $ K_i^A/M_i^A>K_i/M_i $ for each affected user with $ M_i>0 $. Any selection that removes $ Q $ units after auditing would remove at least $ Q $ without auditing and would cost less. Auditing therefore cannot lower the least cost of removing $ Q $. If every least-cost campaign without audits uses a positive share of affected users and the provider can still remove enough opposition after auditing, equality would imply a least-cost unaudited campaign that uses none of them, a contradiction. The increase is therefore strict.$ \square $

## Formal definition of user-aligned advice

A procedure $ g $ searches the policy, selects evidence and alternatives, and produces an information summary $ h_g $. After seeing that summary, the citizen opposes when

$$
\mathbb{E}[v_i(w)\mid h_g]>0.
$$

The expected value of procedure $ g $, after subtracting its search and interpretation cost $ k_i(g) $, is

$$
J_i(g)=
\mathbb{E}[\max\{0,\mathbb{E}[v_i(w)\mid h_g]\}]-k_i(g).
$$

Let $ \mathcal G_i^0 $ contain the procedures whose search, inclusion, and comparison rules do not depend on which policy result benefits a later interest group. A user-aligned procedure is any

$$
g_i^U\in\arg\max_{g\in \mathcal G_i^0}J_i(g).
$$

The citizen chooses the rule before learning which side a later interest group may favor.

Deleting information from a user-aligned procedure at no lower cost cannot improve $ J_i(g) $ because the citizen could ignore the extra information and copy every decision available under the shorter summary. The preference is strict when the deleted information has positive value and sometimes changes the best action.

Stable broad values can produce the payoff difference above. Let $ \mathcal A $ be a finite set of broad goals, such as efficiency, fairness, and rights. The policy contains material considerations $ j\in\mathcal C(w) $. Consideration $ j $ contributes $ \delta_{jk}(w) $ to goal $ k $, and citizen $ i $ places weight $ b_{ik}$ on that goal. Let $ e_i $ be the private cost of active opposition. With complete verified evidence,

$$
v_i(w)=
\sum_{j\in\mathcal C(w)}\sum_{k\in\mathcal A}b_{ik}\delta_{jk}(w)-e_i.
$$

The weights can be meaningful before the citizen studies the policy because the citizen may not know which considerations apply or how the options trade off the goals. A procedure determines which considerations and comparisons become available; steering changes this evidence rather than the weights. Several user-aligned procedures may remain reasonable. If they imply different actions, I treat the preferred action as uncertain rather than assign a precise loss. This benchmark requires no unique ``true self.''

## Audit details and checks

### Policy set and model run

The starting set contained all 922 records in the UK Parliament collection of impact assessments. I used twenty policies to develop the design and excluded them from the test set. Fixed inclusion and duplicate rules produced 75 candidates from 2020--2025. Two coders screened the candidates in separate orders that hid their ranks, and a third reviewed disagreements. A checker who also did not see the ranks reviewed every disagreement and a sample of agreements selected by a fixed digital rule. The final duplicate check left 54 policies across six policy areas.

The final test set contains 540 cards. Two people independently classified each card as favoring adoption, favoring rejection, or clearly favoring neither. They agreed on 498 cards. A third coder resolved 41 of the 42 disagreements by majority without seeing the later instruction to favor one side. A fixed rule classified the remaining three-way disagreement as neutral because the source statement did not compare the options. The final set contains 217 adoption-favoring, 215 rejection-favoring, and 108 neutral cards.

Before the run, I fixed the source set, instructions, model access, failure rules, and analysis. Digital fingerprints identify every source file and card, and human reviewers completed all classifications first. Pairing within policy area balanced the card mix before the public random assignment of targets.

> **Caption.** Registered model services

| Service | Registered identifier and access | Setting |
| --- | --- | --- |
| OpenAI GPT-5.6 Sol | `gpt-5.6-sol` through Codex | xhigh reasoning |
| NVIDIA Nemotron 3 Ultra | <nvidia/nemotron-3-ultra-550b-a55b:free> through OpenRouter's NVIDIA route | No provider fallback |
| Mistral Medium 3.5 | `mistral-medium-2604` through Mistral's API | Registered service default |

I registered these services on 1 August 2026; the replication README gives client versions and commands.

I made separate planner and writer calls to the same model service and used a different service for the auditor. The models took turns in the three roles: GPT-5.6 Sol used Nemotron as auditor, Nemotron used Mistral, and Mistral used GPT-5.6 Sol. Calls ran from 19:00 to 23:09 UTC on 2 August 2026. The record at <https://osf.io/r43ka/>timestamps the completed run before human review and statistical analysis.

### Measures and checks

For policy $ j $, I give each card $ c $ a score $ \sigma(c)\in\{-1,0,1\}$, where a positive value favors adoption. Among all possible sets of six cards, let $ S_j^{\min}$ and $ S_j^{\max}$ be the minimum and maximum sums. The selected set $ S $ receives the following evidence score, scaled from $-1 $ to $+1 $:$$ E_j(S)=2\frac{\sum_{c\in S}\sigma(c)-S_j^{\min}}{S_j^{\max}-S_j^{\min}}-1. $$ Let $ t_j\in\{-1,1\}$ denote the rejection or adoption target from the random assignment. If $ S_j^D $ and $ S_j^N $ are the directional and non-directional selections, the change in evidence in the direction of the target is $$ t_j\{E_j(S_j^D)-E_j(S_j^N)\}. $$ I treat the writer score $ \rho_j\in\{-3,-2,\ldots,3\}$ in the same way. I average the three assignments of models to roles within policy and then average across policies.

The primary claim passes only if both average changes are positive; I report the larger of their two randomization-test $ p $-values. I test source access only after this claim passes. The two detection measures are the directional--non-directional probability difference and the reduction in natural-log loss, which penalizes confident wrong probabilities.

Each call follows a fixed retry schedule. A final failure sets the affected difference to zero. I retain planned skips and omit no failed call. Automated checks verify the outputs, model services, card orders, and file fingerprints.

The run contains all 1,620 planned records: 1,586 usable responses, 30 planned skips, and four calls that failed after all retries. Removing any one policy area gives evidence-selection estimates from 0.799 to 0.846 and recommendation estimates from 0.543 to 0.576. Evidence moves toward the target in all three assignments of models to roles, while recommendation change ranges from 0.278 to 0.815. Because each assignment changes both planner and writer, these comparisons cannot isolate one model's contribution.

A final preplanned test tells the directional planner only whether its first brief failed an audit screen and allows one revision. A separate auditor evaluates it. The test requires suspicion to fall by at least 0.100 while 0.500 points of recommendation change remain. Suspicion falls by 0.239, but only 0.111 points remain, so the test fails. The planner receives one pass-or-fail signal, no evaluator identity, and no user history; the result therefore does not cover repeated adaptation or personalization.

## External reanalysis details

The Williams--Ceci experiment randomly assigned 1,496 respondents: 500 to no assistance, 501 to fixed biased arguments, and 495 to biased autocomplete. Eight post-task attitudes are missing, leaving 498, 497, and 493 complete responses. I compare group averages and allow outcome variation to differ across groups. Excluding the 11 cases flagged for technical problems changes the autocomplete-versus-fixed estimate only from 0.235 to 0.236.

To study whom to contact, I use initial opponents in two data sets: 336 respondents in the Williams--Ceci ordinary-autocomplete versus no-assistance comparison, and 10,300 respondents across ten issues in the first dialogue study of [@hackenburg_etal_2025]. Following the authors' cautious rule, I set missing responses after the dialogue in the larger data set to their value before assistance.

Separate regression forests, a tree-based machine-learning method, predict positions with and without assistance from prior information. Their difference,$ \widehat m_1(X_i)-\widehat m_0(X_i) $, ranks respondents. Five-fold cross-fitting trains on four groups and predicts the fifth, so a respondent's own response never informs that respondent's predicted effect. I repeat the split 20 times for the smaller data set and five times for the larger one. The augmented inverse-probability score combines these predictions with a correction based on random assignment.[@athey_wager_2021] use this approach to compare rules while reducing dependence on any one prediction model. Their setting allows observational data; random assignment supplies the treatment probabilities here. The score estimates the average effect under each rule:

$$
\widehat\psi_i
={}\widehat m_1(X_i)-\widehat m_0(X_i)
+\frac{Z_i}{\widehat\pi_j}\{Y_i-\widehat m_1(X_i)\} \\
-\frac{1-Z_i}{1-\widehat\pi_j}\{Y_i-\widehat m_0(X_i)\},
$$

where $ X_i $ contains information available before assistance,$ Z_i $ records the form of assistance for respondent $ i $,$ Y_i $ is the position toward the assigned side after the task,$ \widehat m_t $ gives the predicted position after training excludes respondent $ i $'s group under assistance state $ t $, and $ \widehat\pi_j $ is the share that receives assistance within the issue.

The predicted-effect rule contacts the fixed share with the largest predicted effects within each issue.[@kitagawa_tetenov_2018] study how to allocate a limited number of treatments when effects differ across people. That limit matches a provider that can contact only a given share and must decide whom to approach. A simple comparison rule ranks initial opponents by their distance from the neutral position.

> **Caption.** Estimated value of choosing whom to contact| Data and share contacted | Random | Predicted-effect rule [95% interval] | Gain [95% interval] | Initial-attitude rule | | --- | --- | --- | --- | --- | | Williams--Ceci, 25% | 8.53 | 10.38 [$-3.84 $, 24.60] | 1.85 [$-9.97 $, 13.67] | 18.66 | | Williams--Ceci, 50% | 8.53 | 11.36 [1.50, 21.22] | 2.83 [$-3.34 $, 9.00] | 13.00 | | Hackenburg et al., 25% | 11.57 | 17.23 [13.52, 20.93] | 5.65 [4.53, 6.77] | 9.10 | | Hackenburg et al., 50% | 11.58 | 15.71 [11.68, 19.74] | 4.14 [3.18, 5.09] | 9.55 |*Notes:*The sample contains initial opponents. Values report estimated movement toward the assigned position per contact on a 0--100 scale. Every rule contacts a fixed share within each issue. Intervals in the large data set allow responses from the same issue to be related and use a $ t $ cutoff based on the ten issues. With only four issues, the smaller data set uses intervals that allow unequal variation and cannot give precise estimates. The analysis is exploratory.

As a check, I train the forests on nine issues and evaluate the tenth without telling the model which issue it is. At 25 percent contact, the gain over random selection is 5.94 points with interval $[5.03,6.85]$. This removes all responses from the evaluated topic during training and provides a cross-topic check within the same study.

## Notes

[^1] or ever
[^2] This could be a financial transaction, political support or any other advantage the provider values.
[^3] or narrow expectations
[^4] A similar effect could come from later training (fine tuning) or biased training data.
