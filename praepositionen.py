import random

preps = {
    "denken": "an",
    "schreiben": "an",
    "sich wenden": "an",
    "achten": "auf",
    "Antwort": "auf",
    "stolz sein": "auf",
    "verzichten": "auf",
    "warten": "auf",
    "sich vorbereiten": "auf",
    "Blick": "auf",
    "sich freuen (DEVE SUCCEDERE)": "auf",
    "unterstreichen": "durch",
    "danken": "fur",
    "sich interessieren": "fur",
    "berichten": "uber",
    "entscheiden": "uber",
    "erzaehlen": "uber, von",
    "sich freuen (SUCCESSO)": "uber",
    "sich informieren": "uber",
    "reden": "uber",
    "sprechen": "uber, von",
    "streiten": "uber",
    "diskutieren": "uber",
    "sich einigen": "uber",
    "sich beschweren": "uber",
    "sich aergern": "uber",
    "sich bewerben": "um",
    "bitten": "um",
    "sich handeln": "um",
    "sich kuemmern": "um",
    "leiden": "an",
    "bestehen": "aus",
    "sich beschaeftigen": "mit",
    "telefonieren": "mit",
    "sich treffen": "mit",
    "sich verabreden": "mit",
    "enden": "mit",
    "zufrieden sein": "mit",
    "einverstanden sein": "mit",
    "fragen": "nach",
    "sich erkundigen": "nach",
    "handeln": "von",
    "halten": "von",
    "profitieren": "von",
    "ueberzeugt sein": "von",
    "Angst": "vor",
    "einladen": "zu",
    "Einladung": "zu",
    "gehoeren": "zu",
    "gratulieren": "zu",
    "passen": "zu",
    "ueberreden": "zu",
}
verbs = ["denken", "sich wenden", "achten", "Antwort", "stolz sein", "verzichten", "warten", "unterstreichen", "danken", "sich interessieren", "berichten", "entscheiden", "erzaehlen", "sich freuen (DEVE SUCCEDERE)", "sich informieren", "reden", "sprechen", "streiten", "sich bewerben", "bitten", "sich handeln", "sich kuemmern", "leiden", "bestehen", "sich beschaeftigen", "telefonieren", "sich treffen", "sich verabreden", "fragen", "handeln", "Angst", "einladen", "Einladung", "gehoeren", "gratulieren", "passen", "schreiben", "sich freuen (SUCCESSO)", "sich vorbereiten", "Blick", "diskutieren", "sich einigen", "sich beschweren", "sich aergern", "enden", "zufrieden sein", "einverstanden sein", "sich erkundigen", "halten", "profitieren", "ueberzeugt sein", "ueberreden"]
 
random.shuffle(verbs)

i = 0
mistakes = 0
while i!=len(verbs):
    verb = verbs[i]
    ans = str(input(verb + ": "))

    if ans != preps[verb]:
        mistakes += 1

    print(preps[verb])
    print("Left:", len(verbs)-i, " mistakes:", mistakes)
    print()
    i+=1
