import random
import tkinter as tk
import math

BG = "#07090d"
CARD_BG = "#000000"  # Black card like the image
CARD_INNER = "#000000"
TEXT = "#ffffff"  # White text
MUTED = "#aab4c3"
ACCENT = "#4db6ff"
BORDER = "#000000"
BUTTON = "#141a22"
BUTTON_ACTIVE = "#1d2631"
EASY_COLOR = "#1a3a24"
MEDIUM_COLOR = "#4a3f16"
HARD_COLOR = "#4a2416"

CHAPTER_ORDER = [
    "Foundation",
    "Informed consent",
    "Children and medical decision-making",
    "Human Experimentation",
    "Physician-Assisted Death",
    "Reproductive Ethics and Family Formation",
    "Medical tourism",
    "Psychiatry, Mental illness, and Paternalism",
    "Military Medicine",
    "Pandemic Ethics, Quarantine, and Biosecurity",
    "Genetics, biobanks, and the right not to know",
    "AI and Brain-computer Interfaces",
    "Future-Oriented Medicine",
    "Patients as Art and Diagnostic Observation",
]

ALL_CHAPTERS = "All Chapters"
ALL_DIFFICULTIES = "All"

TOPIC_BANK = {
    "Foundation": {
        "easy": [
            ("What does medical ethics study?", "What is right and wrong in medicine."),
            ("What hidden thing does ethics often expose?", "Assumptions."),
            ("What power question does ethics ask?", "Who decides."),
            ("When is ethics especially useful?", "When the right action is not obvious."),
            ("What does ethics help sort through?", "Uncertainty."),
            ("What body-related issue keeps appearing in medical ethics?", "Control over one's own body."),
            ("What does ethics examine besides actions?", "Power relationships."),
            ("What can ethics challenge once assumptions are named?", "Unjustified authority."),
            ("Why is ethics not optional in medicine?", "Because medicine often allows more than one possible action."),
            ("What major system often develops alongside ethics?", "Law."),
        ],
        "medium_concepts": [
            ("hidden assumptions", "Ethics makes unspoken assumptions visible so they can be judged."),
            ("power", "Medical ethics asks who has authority, who is vulnerable, and how power is used."),
            ("uncertainty", "Ethics matters most when medicine is not mechanically obvious."),
            ("control", "The topic keeps returning to who can recommend, refuse, or override treatment."),
            ("law", "Legal cases help trace how ethical ideas become enforceable rules."),
            ("rights", "American medical ethics often emphasizes rights, limits on state power, and bodily freedom."),
        ],
        "hard": [
            ("Why does this chapter treat ethics as more than behavior review?", "Because it also studies assumptions, institutions, and power."),
            ("What is the deeper issue behind asking whether an action was good or bad?", "Whether the person deciding had justified authority."),
            ("What makes ethics necessary even when medicine has technical knowledge?", "Technical knowledge alone does not settle competing values."),
            ("What does it mean to say ethics is part of medicine itself?", "It helps decide what should be done when more than one path is possible."),
            ("Why can unethical conduct survive for a long time?", "Because it hides inside assumptions nobody names."),
            ("What kind of conflict makes ethical analysis urgent?", "A conflict between authority and control over the body."),
            ("What institutional question sits underneath many medical disputes?", "When institutions may override individuals."),
            ("Why are legal cases useful in this chapter?", "They show changing ethical limits in concrete decisions."),
            ("What does this chapter connect ethics to besides doctors and patients?", "The state, institutions, and systems of authority."),
            ("What is the most exam-important shift in this chapter?", "From surface actions to the deeper structure of power and justification."),
        ],
    },

    "Informed consent": {
        "easy": [
            ("What is real consent?", "Permission joined with understanding."),
            ("Is a signed form enough by itself?", "No."),
            ("What body principle is central here?", "Bodily integrity."),
            ("Who normally decides what happens to an adult patient's body?", "The adult patient of sound mind."),
            ("What is medical battery?", "Unauthorized medical touching or treatment."),
            ("What famous issue separates consent to examination from consent to surgery?", "They are not the same consent."),
            ("What kind of risks must be disclosed?", "Material risks."),
            ("What makes a risk material?", "A reasonable person would care about it."),
            ("Does informed consent require every tiny detail?", "No."),
            ("What is the basic purpose of informed consent?", "To protect meaningful patient choice."),
        ],
        "medium_concepts": [
            ("understanding", "Consent is only valid if the patient actually understands enough to choose."),
            ("bodily integrity", "The law protects the patient's control over what is done to the body."),
            ("battery", "Treatment without valid consent can count as a legal wrong even if medically skillful."),
            ("emergency exception", "Doctors may act without consent when delay is impossible and the patient cannot choose."),
            ("material risk", "Disclosure focuses on risks that matter to a real decision, not every remote possibility."),
            ("patient-centered disclosure", "The point is what a reasonable patient would need to know, not what the physician prefers to say."),
        ],
        "hard": [
            ("Why is a signed consent form weaker than many students think?", "Because paperwork can exist without real understanding."),
            ("What is the deeper value protected by informed consent?", "Control over one's own body."),
            ("Why is the emergency exception narrow?", "Because it excuses lack of consent only when real choice is impossible."),
            ("What key limit did the older battery cases establish?", "Consent to one procedure is not blanket consent to another."),
            ("Why does materiality matter so much?", "It decides what must actually be disclosed."),
            ("What does this chapter reject about physician authority?", "That the doctor may decide for the patient simply because the doctor knows more."),
            ("Why is full disclosure of everything not the rule?", "Because informed choice requires relevance, not endless detail."),
            ("What kind of patient standard drives modern disclosure?", "What matters to a reasonable chooser."),
            ("What turns a medical encounter into an autonomy issue?", "When treatment proceeds without meaningful authorization."),
            ("What is the cleanest exam summary of informed consent?", "Respect for bodily choice through understanding, not mere signatures."),
        ],
    },

    "Children and medical decision-making": {
        "easy": [
            ("Why are children a special ethics topic?", "Because decision-making is shared among child, parent, and society."),
            ("Who are the three main parties here?", "Child, parent, and society."),
            ("Do children have full adult autonomy?", "No."),
            ("What affects how much weight a child's view gets?", "Maturity."),
            ("Why is vaccination a major issue in this topic?", "It combines child welfare and public health."),
            ("Why is polio heavily discussed?", "It shows fear, urgency, and child vulnerability."),
            ("Who usually makes medical decisions for children?", "Parents or guardians."),
            ("Can parental refusal ever become unacceptable?", "Yes."),
            ("What basic limit constrains parental choice?", "The child's safety and welfare."),
            ("Why is research with children ethically harder?", "Because the subject is vulnerable and cannot consent like an adult."),
        ],
        "medium_concepts": [
            ("developing autonomy", "Child choice matters, but it is still emerging and tied to maturity."),
            ("parental authority", "Parents usually decide, but their power is not unlimited."),
            ("state interest", "Society may step in when child welfare or public safety is threatened."),
            ("polio trials", "The polio vaccine trials show large-scale pediatric research under public pressure."),
            ("massive consent", "Large pediatric trials raise difficult questions about who can authorize participation."),
            ("risk threshold", "Parents may refuse some things, but not choices that impose unacceptable danger on the child."),
        ],
        "hard": [
            ("Why does this chapter resist a simple parent-versus-child model?", "Because society is a third decision-maker."),
            ("What is the hardest autonomy issue with children?", "How to respect developing choice without pretending it is adult-level choice."),
            ("Why is pediatric research ethically distinct from adult research?", "Because permission and vulnerability are structured differently."),
            ("What made the polio trials ethically powerful beyond science?", "They joined public fear, child risk, and urgency for prevention."),
            ("Why is child refusal not always decisive?", "Because capacity and danger matter."),
            ("What does this chapter say parental rights are not?", "Absolute."),
            ("When does society become more willing to override parents?", "When the child's risk becomes unacceptable."),
            ("What does the polio story reveal about public-health ethics?", "Emergency and social fear can reshape what seems acceptable."),
            ("Why is maturity central rather than just age labels?", "Because real decision-making ability develops unevenly."),
            ("What is the core tension in child medical ethics?", "Protection versus emerging autonomy."),
        ],
    },

    "Human Experimentation": {
        "easy": [
            ("What is the first principle of the Nuremberg Code?", "Voluntary consent is absolutely essential."),
            ("What does human experimentation become without real consent?", "Abuse."),
            ("Why is Nazi experimentation central here?", "It shows how medicine can become domination."),
            ("What must valid consent include?", "Capacity, freedom, and understanding."),
            ("Should research have social value?", "Yes."),
            ("Should unnecessary suffering be avoided?", "Yes."),
            ("Can a subject stop participation?", "Yes."),
            ("Must the researcher ever stop the study?", "Yes, if danger becomes too great."),
            ("Why is Tuskegee studied?", "Because treatment was withheld from vulnerable subjects."),
            ("What major modern protection grew from these abuses?", "Stronger informed-consent and subject protections."),
        ],
        "medium_concepts": [
            ("voluntary consent", "Research is illegitimate if subjects are coerced or uninformed."),
            ("social value", "Risk to humans must be justified by meaningful scientific purpose."),
            ("prior knowledge", "Human studies should not begin recklessly without preparation."),
            ("suffering", "Nuremberg insists on avoiding unnecessary physical and mental harm."),
            ("subject withdrawal", "Participants keep the right to stop at any point."),
            ("researcher duty", "Investigators must stop when danger exceeds ethical limits."),
        ],
        "hard": [
            ("Why is Nuremberg not just history?", "Because it defines the moral floor for human research."),
            ("What does this chapter show about medicine under corrupt power?", "It can shift from healing to control and cruelty."),
            ("Why is consent alone not enough to justify research?", "Because worthless or reckless studies still exploit subjects."),
            ("What makes Tuskegee especially shocking after penicillin?", "An effective treatment existed and was still withheld."),
            ("Why is withdrawal so important?", "Because research subjects remain persons, not instruments."),
            ("What deeper lesson comes from Nazi medicine?", "Professional status does not prevent moral collapse."),
            ("What does this chapter say about scientific gain versus human welfare?", "Welfare must not be sacrificed for data."),
            ("Why is structural ethics important here?", "Because abusive systems, not only bad individuals, enabled the crimes."),
            ("What separates ethical research from mere human use?", "Respect, proportionality, and real consent."),
            ("What is the cleanest exam summary of this chapter?", "No human subject may be reduced to a tool for knowledge."),
        ],
    },

    "Physician-Assisted Death": {
        "easy": [
            ("What is the central question in physician-assisted death?", "Whether medicine may help a person die without abandoning care."),
            ("Does Oregon allow euthanasia?", "No."),
            ("Who performs the final act in Oregon PAS?", "The patient."),
            ("Who is eligible in general terms?", "A capable adult with terminal illness under the law's conditions."),
            ("What kind of prognosis is required in Oregon?", "Expected death within six months."),
            ("How many oral requests are required?", "Two."),
            ("Is a written request also required?", "Yes."),
            ("What must be discussed before PAS proceeds?", "Comfort care, hospice, and pain control."),
            ("Why are two physicians involved?", "To confirm diagnosis, prognosis, and capacity."),
            ("What major value supports PAS?", "Autonomy."),
        ],
        "medium_concepts": [
            ("self-administration", "The law distinguishes assisted death from euthanasia by making the patient perform the final act."),
            ("capacity", "The patient must be capable of making healthcare decisions."),
            ("terminal prognosis", "Eligibility is tied to a limited life expectancy."),
            ("procedural safeguards", "Multiple requests and waiting periods aim to slow rushed decisions."),
            ("alternatives", "Hospice, comfort care, and pain control must be reviewed first."),
            ("role of medicine", "The debate centers on whether helping death fits or corrupts the healer's role."),
        ],
        "hard": [
            ("Why is the final act legally important in PAS?", "It marks the difference between physician assistance and direct killing."),
            ("What does this chapter show about autonomy limits?", "Even autonomy is filtered through procedure, prognosis, and capacity."),
            ("Why are safeguards central rather than decorative?", "Because the law is trying to prevent impulsive or impaired decisions."),
            ("What is the cleanest pro-PAS argument?", "A competent dying person should control the manner of death."),
            ("What is the cleanest anti-PAS argument?", "Medicine should not cross into facilitating death."),
            ("Why does palliative care matter so much in this debate?", "Because some suffering may be relieved without assisted death."),
            ("What fear about prognosis appears in PAS debates?", "That doctors can be wrong."),
            ("Why is psychological evaluation relevant?", "Because impaired judgment can distort a life-ending choice."),
            ("What does this chapter reveal about law and ethics?", "A legal permission can still remain morally contested."),
            ("What is the core tension in one line?", "Autonomy and mercy versus the moral boundaries of medicine."),
        ],
    },

    "Reproductive Ethics and Family Formation": {
        "easy": [
            ("What broad question frames this chapter?", "Whether reproduction is only private or also social and political."),
            ("What major technology is central here?", "IVF."),
            ("Why is IVF discussed in China?", "Because it is tied to both infertility care and demographic policy."),
            ("What kind of burden does IVF place on patients?", "Physical, emotional, social, and financial burden."),
            ("Is one IVF round guaranteed to work?", "No."),
            ("Can access exist on paper but still be hard in practice?", "Yes."),
            ("Who often carries the heaviest burden in infertility treatment?", "Women."),
            ("What social pressure can infertility create?", "Family pressure and stigma."),
            ("Why does the state care about fertility in this chapter?", "Because of aging populations and declining births."),
            ("What older policy shadows the discussion?", "The one-child policy."),
        ],
        "medium_concepts": [
            ("IVF as policy", "The chapter treats IVF not only as treatment but as part of demographic strategy."),
            ("unequal access", "Availability can still be limited by cost, geography, and incomplete support."),
            ("gendered burden", "Women often bear more of the bodily and social cost of fertility treatment."),
            ("social pressure", "Infertility affects identity, marriage, and family expectations."),
            ("success rates", "Repeated cycles may be necessary because one round often fails."),
            ("private versus political", "Reproduction in this chapter is shaped by both intimate choice and state interests."),
        ],
        "hard": [
            ("Why is this chapter not just about having children?", "Because it is also about policy, inequality, and social pressure."),
            ("What makes IVF ethically more than a neutral technology?", "It is embedded in cost, gender, and state goals."),
            ("Why can support for IVF still leave people excluded?", "Because treatment can remain too expensive or hard to reach."),
            ("What is the central justice issue in this chapter?", "Who can realistically access family formation technologies."),
            ("Why does infertility carry more than medical pain?", "It can reshape status, relationships, and self-worth."),
            ("What is the chapter's deeper political point?", "Reproduction can become a tool of population management."),
            ("Why is the burden especially gendered?", "Because treatment often falls more heavily on women physically and socially."),
            ("What does this chapter show about reproductive freedom?", "It is constrained by money, policy, and social expectation."),
            ("Why does historical policy still matter here?", "Past state control shapes current reproductive ethics."),
            ("What is the core tension in one line?", "Private family formation inside public demographic pressure."),
        ],
    },

    "Medical tourism": {
        "easy": [
            ("What is medical tourism?", "Traveling to another country for health care."),
            ("Why do people seek medical tourism?", "Lower cost, faster access, or unavailable care."),
            ("Is medical tourism only about cheap surgery?", "No."),
            ("Can controversial care also be part of medical tourism?", "Yes."),
            ("Why is follow-up a problem?", "Care may be fragmented across borders."),
            ("What infection risk is emphasized?", "Drug-resistant infections."),
            ("Why does inequality matter here?", "Some people can cross borders more easily than others."),
            ("Why are organ markets especially troubling?", "They exploit vulnerable people."),
            ("What happens to records and continuity of care across borders?", "They can be weak or incomplete."),
            ("What is the big ethical conflict here?", "Individual benefit versus broader harm and injustice."),
        ],
        "medium_concepts": [
            ("cost and speed", "Patients often leave because local systems are too slow or expensive."),
            ("controversial care", "Travel may be used to obtain care restricted or unavailable at home."),
            ("continuity", "Aftercare can be poor when the treatment and follow-up happen in different systems."),
            ("infection risk", "Cross-border care can increase exposure to resistant organisms."),
            ("local justice", "Private benefit for outsiders may not strengthen care for local people."),
            ("global inequality", "Mobility itself is uneven, so benefits cluster in people with more money and freedom."),
        ],
        "hard": [
            ("Why is medical tourism not simply consumer choice?", "Because cross-border care can shift burdens onto weaker systems."),
            ("What makes follow-up ethically serious rather than just inconvenient?", "Complications may return to a different system with missing information."),
            ("Why do organ markets stand out even inside medical tourism?", "Because they turn vulnerable bodies into sources of profit."),
            ("What does this topic reveal about inequality?", "The ability to travel for care is itself a privilege."),
            ("Why can a patient benefit while the system worsens?", "Because individual gains may coexist with local displacement or exploitation."),
            ("What is the hidden public-health issue in medical tourism?", "Cross-border spread of resistant infection."),
            ("Why is unavailable care ethically different from cheaper care?", "It may reflect legal, political, or moral evasion rather than price alone."),
            ("What is the cleanest justice question here?", "Who bears the cost of someone else's cross-border treatment choice."),
            ("Why is this chapter linked to globalization?", "Because medical access increasingly follows money and mobility across borders."),
            ("What is the core tension in one line?", "Personal access versus structural inequity."),
        ],
    },

    "Psychiatry, Mental illness, and Paternalism": {
        "easy": [
            ("What main question frames this chapter?", "When protection is justified and when it becomes wrongful control."),
            ("Why is psychiatry especially tied to paternalism?", "Because judgment and capacity are often disputed."),
            ("Why do many physicians avoid mental health care for themselves?", "Stigma and professional fears."),
            ("What is covert medication?", "Hiding medication in food or drink."),
            ("What is one major problem with covert medication?", "It uses deception."),
            ("What is one argument for covert medication?", "It may protect a patient when no safer option exists."),
            ("What is a Ulysses contract?", "A prior agreement allowing future intervention during relapse."),
            ("What practical problem often appears in psychiatry?", "Nonadherence."),
            ("Why is trust so important in psychiatry?", "Because treatment often depends on ongoing cooperation."),
            ("Why is this chapter cautious about psychiatric power?", "Because psychiatry has a history of overreach."),
        ],
        "medium_concepts": [
            ("paternalism", "The chapter asks when overriding present wishes can be justified for safety or welfare."),
            ("stigma", "Fear of exposure or career harm can stop even physicians from seeking mental health care."),
            ("covert medication", "It may avoid restraint, but it also risks betrayal and damaged trust."),
            ("nonadherence", "Refusal or inconsistency creates practical and ethical pressure in treatment."),
            ("Ulysses contracts", "Earlier stable choices may be used to guide care during later relapse."),
            ("history of abuse", "Past psychiatric overreach makes modern coercion especially suspect."),
        ],
        "hard": [
            ("Why is psychiatry uniquely vulnerable to paternalism?", "Because the patient's judgment itself may become the disputed issue."),
            ("What makes covert medication more than a simple kindness?", "It trades truthfulness and trust for possible protection."),
            ("Why are Ulysses contracts controversial?", "Because earlier wishes may conflict with present refusal."),
            ("What is the deepest tension in this chapter?", "Autonomy versus beneficent control under uncertainty about capacity."),
            ("Why does history matter so much in psychiatry?", "Past abuses make present coercion ethically harder to justify."),
            ("Why is nonadherence not just a practical annoyance?", "It can trigger decisions about force, deception, or override."),
            ("What does this chapter reveal about mental health privacy?", "People may avoid care when help seems professionally risky."),
            ("Why can paternalism feel justified yet dangerous here?", "Because protection can slide into domination."),
            ("What is the chapter's sharpest warning?", "Psychiatric power can easily exceed what ethics permits."),
            ("What is the core one-line summary?", "Protection is sometimes needed, but psychiatric control is morally hazardous."),
        ],
    },

    "Military Medicine": {
        "easy": [
            ("What is enhancement in this chapter?", "Improving performance beyond restoring health."),
            ("Why is military consent difficult?", "Hierarchy weakens voluntariness."),
            ("What kinds of functions may enhancement target?", "Fatigue, senses, cognition, movement, and resilience."),
            ("Why are stimulants discussed?", "They are older examples of enhancement."),
            ("What is one major risk of enhancement drugs?", "Addiction or impaired judgment."),
            ("Why is pain reduction ethically risky in war?", "It may reduce restraint."),
            ("What long-term issue can implants raise?", "Permanent harm."),
            ("What fairness issue appears between enhanced and non-enhanced soldiers?", "Unequal risk and cohesion problems."),
            ("Why is accountability a problem with enhancement?", "Control and responsibility may blur."),
            ("What older military medical duty still matters?", "Treat the wounded humanely."),
        ],
        "medium_concepts": [
            ("hierarchy", "Military rank structures make free refusal harder than in ordinary medicine."),
            ("performance targets", "Enhancement aims at stamina, perception, cognition, and combat effectiveness."),
            ("side effects", "Performance gains can bring addiction, aggression, or judgment failure."),
            ("fairness", "Enhancement can alter burdens, expectations, and relationships inside a unit."),
            ("identity after service", "Permanent modifications can complicate return to civilian life."),
            ("responsibility", "If enhancement changes action or control, moral and legal blame become harder to assign."),
        ],
        "hard": [
            ("Why is military enhancement called an ethical vacuum in some discussions?", "Because capability has moved faster than settled moral limits."),
            ("Why is consent in the military weaker than civilian consent?", "Orders and hierarchy pressure compliance."),
            ("What makes enhancement different from treatment?", "Its goal is to exceed normal functioning, not restore it."),
            ("Why is emotion suppression dangerous in war?", "It may remove restraints that normally limit harm."),
            ("What fairness problem appears when only some soldiers are enhanced?", "Risk, expectation, and unit cohesion may become distorted."),
            ("Why are long-term harms especially important here?", "Because the military benefit may end long before the bodily cost does."),
            ("What does this chapter show about means and ends?", "National goals can pressure medicine into serving performance over personhood."),
            ("Why is accountability a deep problem?", "An altered soldier may not cleanly fit old models of responsibility."),
            ("What older stimulant examples teach the main lesson?", "Short-term performance gains can hide severe moral and medical costs."),
            ("What is the core tension in one line?", "Military advantage versus the moral limits of altering human beings for war."),
        ],
    },

    "Pandemic Ethics, Quarantine, and Biosecurity": {
        "easy": [
            ("What is the central conflict in pandemic ethics?", "Public safety versus personal liberty."),
            ("What does quarantine do?", "Separates infected or exposed people to stop spread."),
            ("Where does the word quarantine come from?", "Italian for forty days."),
            ("Why can liberty be limited during outbreaks?", "Because one person's movement can endanger many others."),
            ("What is zoonotic spillover?", "Animal-to-human spread of microbes."),
            ("Why do animal reservoirs matter?", "They allow pathogens to persist and return."),
            ("Why is transparency important in outbreaks?", "Delay and secrecy worsen spread."),
            ("What do healthcare workers need during outbreaks?", "Honest warning and real protection."),
            ("Why is plague often used in this chapter?", "It shows the history of quarantine and fear."),
            ("What broad danger is part of biosecurity?", "Biological threat amplified by science, secrecy, or poor oversight."),
        ],
        "medium_concepts": [
            ("quarantine", "The chapter asks when restricting liberty is justified to prevent harm to others."),
            ("public health power", "The state may intervene more aggressively when infection threatens many people."),
            ("zoonotic reservoirs", "Pathogens in animals complicate control because they can spill back into humans."),
            ("transparency", "Early warning is ethically crucial because secrecy wastes precious response time."),
            ("worker protection", "Institutions owe truthful risk communication and protective support to staff."),
            ("biosecurity", "Anthrax and other cases show how biology plus weak oversight can become a public threat."),
        ],
        "hard": [
            ("Why is quarantine ethically different from ordinary state control?", "Because it restricts liberty to prevent direct infectious harm to others."),
            ("What does this chapter reveal about liberty?", "It is powerful but not unlimited when disease is contagious."),
            ("Why is secrecy morally dangerous in outbreaks?", "It converts delay into wider transmission and lost trust."),
            ("Why do animal reservoirs make pandemic control harder?", "Eliminating human cases may still leave the source intact."),
            ("What is the deepest justice concern in quarantine?", "Whether burdens are imposed fairly and proportionately."),
            ("Why are healthcare workers central ethical figures in outbreaks?", "They bear risk on behalf of the public."),
            ("What does the Honolulu example show in one line?", "Disease control can become discriminatory and destructive."),
            ("Why is outbreak ethics never just clinical medicine?", "Because it also involves law, coercion, and population-level tradeoffs."),
            ("What is the biosecurity lesson beyond natural disease?", "Human systems can magnify biological danger."),
            ("What is the core tension in one line?", "Collective survival versus individual freedom."),
        ],
    },

    "Genetics, biobanks, and the right not to know": {
        "easy": [
            ("What is a biobank?", "A repository of records, tissue, and genetic information."),
            ("What major autonomy claim appears in this chapter?", "The right not to know."),
            ("Why can stored samples create new ethical issues later?", "They may reveal actionable personal findings."),
            ("What is the disclosure dilemma here?", "Whether researchers should recontact participants."),
            ("Why might someone refuse genetic information?", "Because it can bring anxiety, burden, or practical consequences."),
            ("What line becomes blurry when researchers disclose findings?", "The line between research and medical care."),
            ("Can consent forms warn participants about possible recontact?", "Yes."),
            ("What is a middle-ground approach mentioned in this topic?", "Offer but do not force the information."),
            ("Why does anonymity matter?", "It protects privacy."),
            ("Why does traceability matter?", "It makes warning possible."),
        ],
        "medium_concepts": [
            ("right not to know", "Autonomy may include refusing risk information about future disease."),
            ("recontact duty", "Researchers may feel pressure to warn participants about medically important findings."),
            ("consent forms", "Advance warning in consent can shape what participants should later expect."),
            ("practical burden", "Knowing may create follow-up tests, costs, insurance worries, and emotional stress."),
            ("offering not forcing", "A middle position is to let people choose whether to hear more."),
            ("research-care boundary", "Recontact can push research toward acting like personal medical care."),
        ],
        "hard": [
            ("Why is this chapter not simply pro-disclosure?", "Because life-saving information can also violate a person's refusal."),
            ("What makes biobank findings ethically different from ordinary test results?", "The data were often given for research, not direct care."),
            ("Why is the right not to know a serious claim rather than a preference?", "Because unwanted knowledge can reshape life, family, and future choices."),
            ("What is the chapter's central conflict?", "Duty to warn versus duty to respect refusal and privacy."),
            ("Why do consent forms matter so much here?", "They partly determine whether later contact feels expected or intrusive."),
            ("What does anonymity protect that recontact threatens?", "Distance between the person and the discovered risk."),
            ("Why is 'offering but not forcing' attractive?", "It tries to preserve both benefit and autonomy."),
            ("What does this chapter reveal about research ethics today?", "Stored data can generate obligations long after collection."),
            ("Why is the research-versus-care boundary so important?", "Because the goals of advancing knowledge and treating a person are not identical."),
            ("What is the one-line summary?", "Genetic knowledge can save lives, but it can also violate a person's wish not to know."),
        ],
    },

    "AI and Brain-computer Interfaces": {
        "easy": [
            ("Why is AI rising in healthcare?", "Because medicine has too much information for one person to manage."),
            ("How is AI framed in this chapter?", "As support or partnership, not simple replacement."),
            ("What are Centaur doctors?", "Doctors using human judgment with AI assistance."),
            ("What can AI reduce according to this topic?", "Error and bias."),
            ("What does BCI stand for?", "Brain-computer interface."),
            ("What is one major BCI problem?", "Overstating what the patient can actually decide."),
            ("Why is BCI expectation ethically important?", "False hope can harm people."),
            ("What does invasiveness refer to in BCI?", "How physically burdensome the device or procedure is."),
            ("What cognitive issue appears in BCI use?", "The burden of sustained planning and control."),
            ("Does communication through BCI automatically prove full decisional capacity?", "No."),
        ],
        "medium_concepts": [
            ("information overload", "AI rises because modern medicine generates more data than humans can fully track alone."),
            ("decision support", "AI helps store, retrieve, and correlate information while human judgment remains central."),
            ("augmentation", "The chapter presents AI as improving physicians rather than replacing them."),
            ("bias reduction", "AI may reduce mistakes like anchoring by surfacing patterns humans miss."),
            ("BCI expectation", "Restored communication can tempt people to assume more capacity than is actually shown."),
            ("BCI burden", "Invasiveness and cognitive demand shape whether a device is ethically acceptable."),
        ],
        "hard": [
            ("Why is AI not presented as pure replacement?", "Because the chapter keeps final judgment with humans."),
            ("What is the strongest practical argument for AI in this topic?", "Medicine now exceeds the memory and pattern-tracking limits of individuals."),
            ("Why does bias matter so much in the AI chapter?", "Because diagnostic error can come from human shortcuts like anchoring."),
            ("What makes BCI communication ethically tricky?", "A patient may signal something without proving full decision-making capacity."),
            ("Why is hope itself a risk in BCI?", "Because unrealistic expectations can distort consent and family interpretation."),
            ("What does the chapter say the human still does in AI-supported care?", "Reason, judge, and decide."),
            ("Why is BCI invasiveness a core tradeoff?", "Potential benefit rises alongside burden and risk."),
            ("What is the key one-line summary of the AI part?", "More information can help medicine only if human judgment remains central."),
            ("What is the key one-line summary of the BCI part?", "Communication gain does not equal full autonomy proof."),
            ("What is the overall tension in one line?", "Technological assistance versus overclaiming what machines can ethically justify."),
        ],
    },

    "Future-Oriented Medicine": {
        "easy": [
            ("What major shift defines future-oriented medicine?", "Moving from reacting to symptoms toward predicting risk earlier."),
            ("What can earlier prediction enable?", "Earlier screening, follow-up, and intervention."),
            ("How is genetics used here?", "To estimate future disease risk."),
            ("What is biological age?", "How the body is actually aging."),
            ("What is chronological age?", "How many years a person has lived."),
            ("Name one type of aging clock used here.", "Proteomic organ clocks or epigenetic clocks."),
            ("Why is AI used in this topic?", "To detect predictive patterns humans may miss."),
            ("What is health span?", "Years lived with less disease burden."),
            ("What justice concern appears here?", "Predictive tools may widen inequality."),
            ("What autonomy issue reappears here?", "The right not to know future-risk information."),
        ],
        "medium_concepts": [
            ("early prediction", "The topic shifts medicine from waiting for symptoms to anticipating disease earlier."),
            ("genetics as prediction", "Inherited information is treated as future-risk knowledge, not only present description."),
            ("organ clocks", "Biological aging tools try to estimate vulnerability more precisely than calendar age alone."),
            ("AI prediction", "Machine systems are used to predict diseases such as Alzheimer's, cancer, and heart disease."),
            ("surveillance", "Prediction often leads to monitoring, repeated follow-up, and risk management over time."),
            ("health span", "The real goal is healthier later life, not merely more years alive."),
        ],
        "hard": [
            ("Why is this chapter ethically important rather than just technological?", "Because prediction changes what medicine does to people before they are sick."),
            ("What is the central tension in predictive medicine?", "Prevention benefit versus burden, inequality, and unwanted knowledge."),
            ("Why does biological age matter more than calendar age here?", "Because organs may age unevenly and vulnerability can be hidden."),
            ("What does this chapter say prediction leads to besides knowledge?", "Surveillance and preventive management."),
            ("Why is health span a sharper goal than lifespan?", "Because longer life with heavy disease burden is not the main aim."),
            ("What is the justice risk of predictive tools?", "Early benefits may cluster in already privileged groups."),
            ("Why is the right not to know powerful in this chapter?", "Because future-risk information can produce anxiety and pressure to act."),
            ("What role does AI play in the shift to future-oriented medicine?", "It makes pattern-heavy prediction more feasible."),
            ("What is the cleanest one-line summary of the chapter?", "Medicine is moving from visible disease to managed vulnerability."),
            ("Why is this chapter not just optimistic?", "Because better prediction also expands monitoring, inequality, and emotional burden."),
        ],
    },

    "Patients as Art and Diagnostic Observation": {
        "easy": [
            ("Why use art in medical education?", "To sharpen observation."),
            ("What skill does this chapter train?", "Careful visual interpretation."),
            ("Why does visual diagnosis still matter?", "Medicine still depends on trained seeing."),
            ("What kind of clues are students meant to notice?", "Visible bodily signs of illness."),
            ("Can art help identify nutritional problems?", "Yes."),
            ("Can art help identify infectious disease signs?", "Yes."),
            ("Can art help identify eye or posture abnormalities?", "Yes."),
            ("Is this topic about replacing lab tests?", "No."),
            ("What broad habit does this chapter teach?", "Looking carefully."),
            ("What is the main takeaway?", "Visible details can reveal disease."),
        ],
        "medium_concepts": [
            ("trained seeing", "The chapter treats observation as a skill that can be sharpened through images and art."),
            ("visible clues", "Bodies can show illness through appearance before a machine explains it."),
            ("diagnostic attention", "The point is not art history but disciplined noticing."),
            ("predictive era", "Even with advanced technology, medicine still depends on careful observation."),
            ("pattern recognition", "Visual interpretation helps students connect appearance to possible disease."),
            ("range of conditions", "Art can train recognition of nutritional, infectious, tissue, and eye-related signs."),
        ],
        "hard": [
            ("Why is this chapter placed near future-oriented medicine?", "Because even predictive medicine still relies on careful observation."),
            ("What is the ethical value of trained observation?", "Better seeing can improve diagnosis and patient attention."),
            ("Why is this chapter not superficial?", "Because visible details may carry real clinical meaning."),
            ("What habit does this topic oppose?", "Rushing past the body without really looking."),
            ("Why is art useful rather than random here?", "It slows attention and sharpens interpretation of visible signs."),
            ("What does this chapter reveal about diagnosis?", "Seeing well remains a core medical skill even in high-tech medicine."),
            ("Why is the phrase 'patients as art' easy to misunderstand?", "It is about observation training, not turning patients into objects."),
            ("What is the sharpest exam summary of the topic?", "Medicine still needs disciplined visual judgment."),
            ("Why do examples matter in this chapter?", "They train the link between appearance and illness."),
            ("What is the one-line core tension avoided by this chapter?", "Technology should not erase the human skill of looking carefully."),
        ],
    },
}

MEDIUM_TEMPLATES = [
    ("Why does {concept} matter in this topic?", "{answer}"),
    ("How should you think about {concept} on an exam?", "{answer}"),
    ("What is the ethical importance of {concept} here?", "{answer}"),
    ("What problem does {concept} create in this chapter?", "{answer}"),
    ("What should you connect {concept} to?", "{answer}"),
]

def build_topic_cards(topic_name):
    topic = TOPIC_BANK[topic_name]
    cards = []

    for q, a in topic["easy"]:
        cards.append({"difficulty": "Easy", "question": q, "answer": a})

    for concept, answer in topic["medium_concepts"]:
        for q_template, a_template in MEDIUM_TEMPLATES:
            cards.append({
                "difficulty": "Medium",
                "question": q_template.format(concept=concept),
                "answer": a_template.format(answer=answer),
            })

    for q, a in topic["hard"]:
        cards.append({"difficulty": "Hard", "question": q, "answer": a})

    return cards

FLASHCARDS = {topic: build_topic_cards(topic) for topic in CHAPTER_ORDER}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Ethics Flashcards")
        self.root.geometry("1280x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg=BG)

        self.chapter_var = tk.StringVar(value=CHAPTER_ORDER[0])
        self.difficulty_var = tk.StringVar(value=ALL_DIFFICULTIES)
        self.side_var = tk.StringVar(value="Front")
        self.progress_var = tk.StringVar(value="Card 0 of 0")
        self.status_var = tk.StringVar(value="Choose a chapter and press Start / Restart.")
        self.deck_info_var = tk.StringVar(value="")

        self.cards = []
        self.index = 0
        self.showing_back = False
        self.animating = False
        
        # Drag/swipe tracking
        self.drag_start_x = None
        self.drag_start_y = None
        self.is_dragging = False
        self.drag_threshold = 50  # Minimum pixels to trigger swipe

        self.build_ui()

    def make_button(self, parent, text, command, width=14, bg=None):
        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            bg=bg or BUTTON,
            fg=TEXT,
            activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            padx=10,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        )

    def build_ui(self):
        top = tk.Frame(self.root, bg=BG)
        top.pack(fill="x", padx=16, pady=16)

        left = tk.Frame(top, bg=BG)
        left.pack(side="left", anchor="nw")

        tk.Label(left, text="Chapter", bg=BG, fg=TEXT, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 6))

        options = [ALL_CHAPTERS] + CHAPTER_ORDER
        self.chapter_menu = tk.OptionMenu(left, self.chapter_var, *options)
        self.chapter_menu.config(
            bg=BUTTON, fg=TEXT, activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT, highlightthickness=1,
            highlightbackground=BORDER, font=("Segoe UI", 11), width=42
        )
        self.chapter_menu["menu"].config(
            bg=BUTTON, fg=TEXT, activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT, font=("Segoe UI", 10)
        )
        self.chapter_menu.pack(anchor="w")

        controls = tk.Frame(top, bg=BG)
        controls.pack(side="right", anchor="ne")

        row1 = tk.Frame(controls, bg=BG)
        row1.pack(anchor="e")
        self.make_button(row1, "Start / Restart", self.start_session).pack(side="left", padx=4)
        self.make_button(row1, "Shuffle Again", self.shuffle_again).pack(side="left", padx=4)
        self.make_button(row1, "Random Card", self.random_card).pack(side="left", padx=4)

        row2 = tk.Frame(controls, bg=BG)
        row2.pack(anchor="e", pady=(10, 0))
        self.make_button(row2, "Previous", self.previous_card).pack(side="left", padx=4)
        self.make_button(row2, "Next", self.next_card).pack(side="left", padx=4)

        difficulty_bar = tk.Frame(self.root, bg=BG)
        difficulty_bar.pack(fill="x", padx=16, pady=(0, 10))

        tk.Label(difficulty_bar, text="Difficulty", bg=BG, fg=TEXT, font=("Segoe UI", 11, "bold")).pack(side="left", padx=(0, 10))
        self.make_button(difficulty_bar, "All", lambda: self.set_difficulty(ALL_DIFFICULTIES), width=8).pack(side="left", padx=4)
        self.make_button(difficulty_bar, "Easy", lambda: self.set_difficulty("Easy"), width=8, bg=EASY_COLOR).pack(side="left", padx=4)
        self.make_button(difficulty_bar, "Medium", lambda: self.set_difficulty("Medium"), width=8, bg=MEDIUM_COLOR).pack(side="left", padx=4)
        self.make_button(difficulty_bar, "Hard", lambda: self.set_difficulty("Hard"), width=8, bg=HARD_COLOR).pack(side="left", padx=4)

        tk.Label(difficulty_bar, textvariable=self.deck_info_var, bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(side="right")

        info = tk.Frame(self.root, bg=BG)
        info.pack(fill="x", padx=16, pady=(0, 10))

        tk.Label(info, textvariable=self.side_var, bg=BG, fg=ACCENT, font=("Segoe UI", 11, "bold")).pack(side="left")
        tk.Label(info, text="   ", bg=BG, fg=TEXT).pack(side="left")
        tk.Label(info, textvariable=self.progress_var, bg=BG, fg=TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")
        tk.Label(info, text="   ", bg=BG, fg=TEXT).pack(side="left")
        tk.Label(info, textvariable=self.status_var, bg=BG, fg=MUTED, font=("Segoe UI", 11)).pack(side="left")

        self.canvas = tk.Canvas(self.root, bg=BG, highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        self.canvas.bind("<Configure>", self.on_canvas_resize)
        # Bind mouse events for drag/swipe
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

        self.root.bind("<Left>", lambda e: self.previous_card())
        self.root.bind("<Right>", lambda e: self.next_card())
        # Space bar / Enter flip the card (global so it works regardless of focus)
        self.root.bind_all("<space>", lambda e: self.flip_card())
        self.root.bind("<Return>", lambda e: self.flip_card())
        
        # Store card bounds for click detection
        self.card_bounds = None

        self.card_outer = None
        self.card_inner = None
        self.card_text = None
        self.draw_card(1.0, 0.0, 0)

    def set_difficulty(self, value):
        self.difficulty_var.set(value)
        self.start_session()

    def get_cards_for_selection(self):
        selected_chapter = self.chapter_var.get()
        selected_difficulty = self.difficulty_var.get()

        base_cards = []
        if selected_chapter == ALL_CHAPTERS:
            for chapter in CHAPTER_ORDER:
                for card in FLASHCARDS[chapter]:
                    base_cards.append({
                        "chapter": chapter,
                        "difficulty": card["difficulty"],
                        "question": card["question"],
                        "answer": card["answer"],
                    })
        else:
            for card in FLASHCARDS[selected_chapter]:
                base_cards.append({
                    "chapter": selected_chapter,
                    "difficulty": card["difficulty"],
                    "question": card["question"],
                    "answer": card["answer"],
                })

        if selected_difficulty != ALL_DIFFICULTIES:
            base_cards = [c for c in base_cards if c["difficulty"] == selected_difficulty]

        return base_cards

    def current_card_text(self):
        if not self.cards:
            return "No cards loaded for this chapter/difficulty filter."
        card = self.cards[self.index]
        return card["answer"] if self.showing_back else card["question"]

    def update_labels(self):
        if not self.cards:
            self.side_var.set("Front")
            self.progress_var.set("Card 0 of 0")
            self.status_var.set("No cards in this filter.")
            self.deck_info_var.set("0 cards loaded")
            return

        card = self.cards[self.index]
        chapter = card["chapter"]
        difficulty = card["difficulty"]
        self.progress_var.set(f"Card {self.index + 1} of {len(self.cards)}")
        self.status_var.set(f"Chapter: {chapter} | Difficulty: {difficulty}")

        if self.chapter_var.get() == ALL_CHAPTERS:
            self.deck_info_var.set(f"Using all topics | {len(CHAPTER_ORDER)} chapters")
        else:
            if self.difficulty_var.get() == ALL_DIFFICULTIES:
                self.deck_info_var.set("50 cards in this chapter")
            elif self.difficulty_var.get() == "Easy":
                self.deck_info_var.set("10 easy cards in this chapter")
            elif self.difficulty_var.get() == "Medium":
                self.deck_info_var.set("30 medium cards in this chapter")
            else:
                self.deck_info_var.set("10 hard cards in this chapter")

        self.side_var.set("Back" if self.showing_back else "Front")

    def on_canvas_resize(self, event=None):
        self.draw_card(1.0, 0.0, 0)
    
    def on_mouse_down(self, event):
        """Handle mouse button press - start tracking drag"""
        if not self.cards or self.animating:
            return
        
        # Check if click is on the card
        if self.card_bounds:
            x1, y1, x2, y2 = self.card_bounds
            padding = 10
            if (x1 - padding <= event.x <= x2 + padding and 
                y1 - padding <= event.y <= y2 + padding):
                # Start tracking drag
                self.drag_start_x = event.x
                self.drag_start_y = event.y
                self.is_dragging = True
    
    def on_mouse_drag(self, event):
        """Handle mouse drag - update card position for visual feedback"""
        if not self.is_dragging or not self.cards or self.animating:
            return
        
        # Calculate drag distance
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        
        # Only respond to horizontal drags (swipe left/right)
        if abs(dx) > abs(dy) and abs(dx) > 10:
            # Use the actual drag distance as offset, but limit it
            max_offset = 200  # Maximum pixels to drag
            x_offset = max(-max_offset, min(max_offset, dx))
            
            # Draw card with horizontal offset for visual feedback
            self.draw_card(1.0, 0.0, x_offset)
    
    def on_mouse_up(self, event):
        """Handle mouse button release - check for swipe and trigger action"""
        if not self.is_dragging:
            # If no drag occurred, treat as click and flip card
            if self.card_bounds:
                x1, y1, x2, y2 = self.card_bounds
                padding = 10
                if (x1 - padding <= event.x <= x2 + padding and 
                    y1 - padding <= event.y <= y2 + padding):
                    self.flip_card()
            return
        
        if not self.cards or self.animating:
            self.is_dragging = False
            self.drag_start_x = None
            self.drag_start_y = None
            return
        
        # Calculate total drag distance
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        
        # Check if it's a horizontal swipe (left or right)
        if abs(dx) > abs(dy) and abs(dx) > self.drag_threshold:
            if dx > 0:
                # Swipe right - previous card
                self.previous_card()
            else:
                # Swipe left - next card
                self.next_card()
        else:
            # Not a significant swipe, just redraw card normally
            self.draw_card(1.0, 0.0, 0)
        
        # Reset drag state
        self.is_dragging = False
        self.drag_start_x = None
        self.drag_start_y = None

    def draw_card(self, scale_x=1.0, rotation=0.0, x_offset=0):
        """
        Draw the card with optional 3D flip animation and drag offset
        rotation: 0.0 to 180.0 degrees (0 = front, 180 = back)
        x_offset: horizontal offset in pixels for drag feedback
        """
        self.canvas.delete("all")

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10:
            return

        card_w = int(min(980, w * 0.82))
        card_h = int(min(500, h * 0.78))
        
        # Calculate 3D perspective: width scales based on rotation
        # Convert rotation to radians
        rotation_rad = math.radians(rotation)
        # Use absolute cosine to get the width scale (1.0 at 0°, 0.0 at 90°, 1.0 at 180°)
        perspective_scale = abs(math.cos(rotation_rad))
        # Apply both scale_x (for old animation) and perspective
        scaled_w = max(12, int(card_w * scale_x * perspective_scale))

        # Apply horizontal offset for drag feedback
        x1 = (w - scaled_w) // 2 + x_offset
        y1 = (h - card_h) // 2
        x2 = x1 + scaled_w
        y2 = y1 + card_h
        
        # Store card bounds for click detection
        self.card_bounds = (x1, y1, x2, y2)
        
        # Determine which side to show based on rotation
        # During flip: rotation 0-90 shows original side, 90-180 shows flipped side
        if rotation < 90.0:
            # Show original side
            display_back = self.showing_back
        else:
            # Show flipped side (after 90 degrees)
            display_back = not self.showing_back
        
        radius = 12  # Rounded corner radius
        shadow_offset = 5  # Shadow offset

        # Draw shadow (subtle dark shadow beneath card)
        shadow_x1 = x1 + shadow_offset
        shadow_y1 = y1 + shadow_offset
        shadow_x2 = x2 + shadow_offset
        shadow_y2 = y2 + shadow_offset
        
        # Simple shadow rectangle with rounded corners
        # Shadow top edge
        self.canvas.create_rectangle(shadow_x1 + radius, shadow_y1, 
                                    shadow_x2 - radius, shadow_y1 + radius, 
                                    fill="#0a0a0a", outline="", width=0)
        # Shadow middle
        self.canvas.create_rectangle(shadow_x1, shadow_y1 + radius, 
                                    shadow_x2, shadow_y2 - radius, 
                                    fill="#0a0a0a", outline="", width=0)
        # Shadow bottom edge
        self.canvas.create_rectangle(shadow_x1 + radius, shadow_y2 - radius, 
                                    shadow_x2 - radius, shadow_y2, 
                                    fill="#0a0a0a", outline="", width=0)
        # Shadow rounded corners
        self.canvas.create_oval(shadow_x1, shadow_y1, shadow_x1 + radius * 2, 
                               shadow_y1 + radius * 2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x2 - radius * 2, shadow_y1, shadow_x2, 
                               shadow_y1 + radius * 2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x2 - radius * 2, shadow_y2 - radius * 2, 
                               shadow_x2, shadow_y2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x1, shadow_y2 - radius * 2, 
                               shadow_x1 + radius * 2, shadow_y2, fill="#0a0a0a", outline="", width=0)

        # Draw main card with rounded corners (using polygon approximation)
        # Top edge
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y1 + radius, 
                                    fill=CARD_BG, outline="", width=0)
        # Middle
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, 
                                    fill=CARD_BG, outline="", width=0)
        # Bottom edge
        self.canvas.create_rectangle(x1 + radius, y2 - radius, x2 - radius, y2, 
                                    fill=CARD_BG, outline="", width=0)
        # Rounded corners using ovals
        self.canvas.create_oval(x1, y1, x1 + radius * 2, y1 + radius * 2, 
                               fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x2 - radius * 2, y1, x2, y1 + radius * 2, 
                               fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x2 - radius * 2, y2 - radius * 2, x2, y2, 
                               fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x1, y2 - radius * 2, x1 + radius * 2, y2, 
                               fill=CARD_BG, outline="", width=0)
        
        # Draw card edge when rotating (at 90 degrees, show the edge)
        if 80.0 < rotation < 100.0:  # Near 90 degrees, show the edge
            edge_width = max(2, int(card_w * 0.02 * (1 - perspective_scale)))
            edge_color = "#1a1a1a"  # Dark edge color
            # Draw the card edge (vertical line in the middle)
            edge_x = w // 2
            self.canvas.create_rectangle(
                edge_x - edge_width // 2, y1,
                edge_x + edge_width // 2, y2,
                fill=edge_color, outline="", width=0
            )
        
        # Create a transparent clickable rectangle covering the entire card
        # This ensures clicks anywhere on the card work
        clickable_rect = self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill="", outline="", width=0,
            tags="card_clickable"
        )
        self.canvas.tag_bind("card_clickable", "<Button-1>", lambda e: self.flip_card())

        # Only draw card content if it's visible (not edge-on)
        # Use a threshold to avoid text condensing during flip
        # Text will fade out as card approaches edge-on view
        text_visible = perspective_scale > 0.25
        
        # Calculate text position based on card center (not scaled edges)
        # This keeps text stable during animation
        text_center_x = w // 2
        text_center_y = h // 2
        
        if text_visible:
            
            # Draw "Card" text with card number at top left (positioned relative to card center)
            card_label_x = text_center_x - card_w // 2 + 30
            card_label_y = text_center_y - card_h // 2 + 25
            
            # Get card number
            card_number_text = "Card"
            if self.cards and len(self.cards) > 0:
                card_number_text = f"Card {self.index + 1} of {len(self.cards)}"
            
            self.canvas.create_text(
                card_label_x, card_label_y,
                text=card_number_text,
                fill=TEXT,
                font=("Segoe UI", 14, "normal"),
                anchor="nw"
            )
            
            # Draw flashcard content in center
            # Use full card width for text widget to prevent condensing during animation
            self.card_text = tk.Text(
                self.canvas,
                wrap="word",
                bg=CARD_BG,
                fg=TEXT,
                insertbackground=TEXT,
                relief="flat",
                bd=0,
                font=("Segoe UI", 20),
                padx=30,
                pady=30
            )
            # Get text based on which side we're displaying
            if display_back:
                card = self.cards[self.index] if self.cards and self.index < len(self.cards) else None
                text_content = card["answer"] if card else "No cards loaded."
            else:
                card = self.cards[self.index] if self.cards and self.index < len(self.cards) else None
                text_content = card["question"] if card else "No cards loaded."
            
            self.card_text.insert("1.0", text_content)
            self.card_text.config(state="disabled")
            # Bind click event to Text widget so clicks on text also flip the card
            self.card_text.bind("<Button-1>", lambda e: self.flip_card())

            # Use full card width for text, not scaled width - prevents condensing
            text_w = max(50, card_w - 100)
            text_h = max(50, card_h - 150)

            self.canvas.create_window(
                text_center_x,
                text_center_y,
                window=self.card_text,
                width=text_w,
                height=text_h
            )
            
            # Draw "Chapter" label and chapter name at bottom left
            # Position relative to card center for better flow during animation
            chapter_name = "No Chapter"
            if self.cards and self.index < len(self.cards):
                chapter_name = self.cards[self.index].get("chapter", "No Chapter")
            
            chapter_x = text_center_x - card_w // 2 + 30
            chapter_y_bottom = text_center_y + card_h // 2
            
            self.canvas.create_text(
                chapter_x, chapter_y_bottom - 50,
                text="Chapter",
                fill=TEXT,
                font=("Segoe UI", 11, "normal"),
                anchor="sw"
            )
            self.canvas.create_text(
                chapter_x, chapter_y_bottom - 20,
                text=chapter_name,
                fill=TEXT,
                font=("Segoe UI", 14, "bold"),
                anchor="sw"
            )
            
            # Draw difficulty level at bottom right (EASY, MEDIUM, or HARD)
            difficulty_text = ""
            if self.cards and self.index < len(self.cards):
                difficulty = self.cards[self.index].get("difficulty", "")
                difficulty_text = difficulty.upper() if difficulty else ""
            
            difficulty_x = text_center_x + card_w // 2 - 30
            difficulty_y = text_center_y + card_h // 2 - 35
            self.canvas.create_text(
                difficulty_x, difficulty_y,
                text=difficulty_text,
                fill=TEXT,
                font=("Arial", 18, "bold"),
                anchor="se"
            )

            # Draw FRONT / BACK label at bottom center of the card
            side_label = "BACK" if display_back else "FRONT"
            side_x = text_center_x
            side_y = text_center_y + card_h // 2 - 35
            self.canvas.create_text(
                side_x, side_y,
                text=side_label,
                fill=MUTED,
                font=("Segoe UI", 22, "bold"),
                anchor="s"
            )

    def refresh_card_without_animation(self):
        self.update_labels()
        self.draw_card(1.0, 0.0, 0)

    def animate_3d_flip(self):
        """Animate a 3D card flip like Figma - rotates from 0 to 180 degrees"""
        if self.animating:
            return
        self.animating = True
        
        # Animation parameters
        num_steps = 40  # More steps for smoother rotation
        duration_ms = 500  # Total animation duration
        step_delay = max(8, duration_ms // num_steps)  # Frame delay
        
        def ease_in_out_cubic(t):
            """Smooth easing function for natural motion"""
            if t < 0.5:
                return 4 * t * t * t
            else:
                return 1 - pow(-2 * t + 2, 3) / 2
        
        def animate(i=0):
            if i > num_steps:
                # Animation complete - flip the side state
                self.showing_back = not self.showing_back
                self.update_labels()
                self.draw_card(1.0, 0.0, 0)  # Reset to front view
                self.animating = False
                return
            
            # Calculate progress (0.0 to 1.0)
            progress = i / num_steps
            # Apply easing
            eased = ease_in_out_cubic(progress)
            # Rotate from 0 to 180 degrees
            rotation = eased * 180.0
            
            # Draw card at current rotation
            self.draw_card(1.0, rotation, 0)
            self.root.after(step_delay, lambda: animate(i + 1))
        
        animate()

    def start_session(self):
        self.cards = self.get_cards_for_selection()
        random.shuffle(self.cards)
        self.index = 0
        self.showing_back = False
        self.refresh_card_without_animation()

    def shuffle_again(self):
        if not self.cards:
            self.start_session()
            return
        random.shuffle(self.cards)
        self.index = 0
        self.showing_back = False
        self.refresh_card_without_animation()

    def flip_card(self):
        if not self.cards:
            return
        # Simple instant flip with no animation
        self.showing_back = not self.showing_back
        self.refresh_card_without_animation()

    def next_card(self):
        if not self.cards or self.animating:
            return
        self.index = (self.index + 1) % len(self.cards)
        self.showing_back = False
        self.refresh_card_without_animation()

    def previous_card(self):
        if not self.cards or self.animating:
            return
        self.index = (self.index - 1) % len(self.cards)
        self.showing_back = False
        self.refresh_card_without_animation()

    def random_card(self):
        if self.animating:
            return
        if not self.cards:
            self.start_session()
            return
        self.index = random.randrange(len(self.cards))
        self.showing_back = False
        self.refresh_card_without_animation()

def main():
    root = tk.Tk()
    FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()