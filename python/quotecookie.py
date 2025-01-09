#!/usr/bin/env python3
import optparse
import random

edquotes = ["Give a good idea to a mediocre team, and they will screw it, up. Give a mediocre idea to a great team, and they will either, fix it or come up with something better. If you get the team, right, chances are that they’ll get the ideas right.", "When looking to hire people, give their potential to grow, more weight than their current skill level. What they will be, capable of tomorrow is more important than what they can, do today.", "Always try to hire people who are smarter than you. Always, take a chance on better, even if it seems like a potential, threat.", "If there are people in your organization who feel they are not, free to suggest ideas, you lose. Do not discount ideas from, unexpected sources. Inspiration can, and does, come from, anywhere.", "It isn’t enough merely to be open to ideas from others. Engaging the collective brainpower of the people you work, with is an active, ongoing process. As a manager, you must, coax ideas out of your staff and constantly push them to, contribute.", "There are many valid reasons why people aren’t candid with, one another in a work environment. Your job is to search for, those reasons and then address them.", "Likewise, if someone disagrees with you, there is a reason.Our first job is to understand the reasoning behind their, conclusions.", "Further, if there is fear in an organization, there is a reason, for it—our job is (a) to find what’s causing it, (b) to, understand it, and (c) to try to root it out.", "There is nothing quite as effective, when it comes to shutting, down alternative viewpoints, as being convinced you are, right", "In general, people are hesitant to say things that might rock, the boat. Braintrust meetings, dailies, postmortems, and, Notes Day are all efforts to reinforce the idea that it is okay, to express yourself. All are mechanisms of self-assessment, that seek to uncover what’s real.", "If there is more truth in the hallways than in meetings, you, have a problem.", "Many managers feel that if they are not notified about, problems before others are or if they are surprised in a, meeting, then that is a sign of disrespect. Get over it.", "Careful “messaging” to downplay problems makes you appear, to be lying, deluded, ignorant, or uncaring. Sharing problems, is an act of inclusion that makes employees feel invested in, the larger enterprise.", "The first conclusions we draw from our successes and failures, are typically wrong. Measuring the outcome without, evaluating the process is deceiving.", "Do not fall for the illusion that by preventing errors, you, won’t have errors to fix. The truth is, the cost of preventing, errors is often far greater than the cost of fixing them.", "Change and uncertainty are part of life. Our job is not to, resist them but to build the capability to recover when, unexpected events occur. If you don’t always try to uncover, what is unseen and understand its nature, you will be ill, prepared to lead.", "Similarly, it is not the manager’s job to prevent risks. It is the, manager’s job to make it safe to take them.", "Failure isn’t a necessary evil. In fact, it isn’t evil at all. It is a, necessary consequence of doing something new.", "Trust doesn’t mean that you trust that someone won’t screw, up—it means you trust them even when they do screw up.", "The people ultimately responsible for implementing a plan, must be empowered to make decisions when things go, wrong, even before getting approval. Finding and fixing, problems is everybody’s job. Anyone should be able to stop, the production line.", "The desire for everything to run smoothly is a false goal — it leads to measuring people by the mistakes they make rather, than by their ability to solve problems.", "Don’t wait for things to be perfect before you share them with others. Show early and show often. It’ll be pretty when we, get there, but it won’t be pretty along the way. And that’s as, it should be.", "A company’s communication structure should not mirror its, organizational structure. Everybody should be able to talk to, anybody.", "Be wary of making too many rules. Rules can simplify life for, managers, but they can be demeaning to the 95 percent who, behave well. Don’t create rules to rein in the other 5 percent, — address abuses of common sense individually. This is more, work but ultimately healthier.", "Imposing limits can encourage a creative response. Excellent, work can emerge from uncomfortable or seemingly untenable, circumstances.", "Engaging with exceptionally hard problems forces us to think, differently.", "An organization, as a whole, is more conservative and resistant to change than the individuals who comprise it. Do, not assume that general agreement will lead to change — it, takes substantial energy to move a group, even when all are, on board.", "The healthiest organizations are made up of departments, whose agendas differ but whose goals are interdependent. If, one agenda wins, we all lose.", "Our job as managers in creative environments is to protect, new ideas from those who don’t understand that in order for, greatness to emerge, there must be phases of not-so-greatness. Protect the future, not the past.", "New crises are not always lamentable—they test and, demonstrate a company’s values. The process of problemsolving often bonds people together and keeps the culture in, the present.", "Excellence, quality, and good should be earned words, attributed by others to us, not proclaimed by us about, ourselves.", "Do not accidentally make stability a goal. Balance is more, important than stability.", "Don’t confuse the process with the goal. Working on our, processes to make them better, easier, and more efficient is, an indispensable activity and something we should, continually work on—but it is not the goal. Making the, product great is the goal."]
carnegiequotes = ["Don't criticize, condemn or complain.", "Give honest, sincere appreciation.", "Arouse in the other person an eager want.", "Become genuinely interested in other people.", "Smile.", "Remember that a person's name is to that person the most important sound in any language.", "Be a good listener.", "Encourage others to talk about themselves.", "Talk in terms of the other person's interest.", "Make the other person feel important - and do so sincerely.", "The only way to get the best of an argument is to avoid it.", "Show respect for the other person's opinions.", "Never say, \"You're wrong.\"" , "If you are wrong, admit it quickly and emphatically.", "Begin in a friendly way.", "Get the other person saying, \"Yes, yes\" immediately.", "Let the other person do a great deal of the talking.", "Let the other person feel that the idea is his or hers.", "Try honestly to see things from the other person's point of view.", "Be sympathetic with the other person's ideas and desires.", "Appeal to the nobler motives.", "Dramatize your ideas.", "Throw down a challenge.", "Begin with praise and honest appreciation.", "Call attention to people's mistakes indirectly.", "Talk about your own mistakes before criticizing the other person.", "Ask questions instead of giving direct orders.", "Let the other person save face.", "Praise the slightest and every improvement. Be \"lavish in your praise.\"" , "Give the other person a fine reputation to live up to.", "Use encouragement. Make the fault seem easy to correct.", "Make the other person happy about doing the thing you suggest."]

stevequotes =["If you want to make everyone happy, don't be a leader. Sell ice cream."]

danquotes= ["The Way of the Worrier -  commandment one: \033[1mDon’t Be a Jerk \033[0m - The virtuous cycle that Joseph described (more metta, better decisions, more happiness, and so on) is real. To boot, compassion has the strategic benefit of winning you allies. And then there’s the small matter of the fact that it makes you a vastly more fulfilled person.", "The Way of the Worrier -  commandment two: \033[1m When Necessary, Hide the Zen \033[0m - Be nice, but don’t be a palooka. Even though I’d achieved a degree of freedom from the ego, I still had to operate in a tough professional context. Sometimes you need to compete aggressively, plead your own case, or even have a sharp word with someone. It’s not easy, but it’s possible to do this calmly and without making the whole thing overly personal.", "The Way of the Worrier -  commandment three: \033[1m Meditate \033[0m - Meditation is the superpower that makes all the other precepts possible. The practice has countless benefits— from better health to increased focus to a deeper sense of calm— but the biggie is the ability to respond instead of react to your impulses and urges. We live our life propelled by desire and aversion. In meditation, instead of succumbing to these deeply rooted habits of mind, you are simply watching what comes up in your head nonjudgmentally. For me, doing this drill over and over again had massive off-the-cushion benefits, allowing me—at least 10% of the time— to shut down the ego with a Reaganesque \"There you go again.\"", "The Way of the Worrier -  commandment four: \033[1m The Price of Security Is Insecurity — Until It’s Not Useful \033[0m - Mindfulness proved a great mental thresher for separating wheat from chaff, for figuring out when my worrying was worthwhile and when it was pointless. Vigilance, diligence, the setting of audacious goals— these are all the good parts of “insecurity.” Hunger and perfectionism are powerful energies to harness. Even the much-maligned \"comparing mind\" can be useful. In my view, Buddhists underplay the utility of constructive anguish. In one of his dharma talks, I heard Joseph quote a monk who said something like, “There’s no point in being unhappy about things you can’t change, and no point being unhappy about things you can.” To me, this gave short shrift to the broad gray area where it pays to wring your hands at least a little bit.", "The Way of the Worrier -  commandment five: \033[1mEquanimity Is Not the Enemy of Creativity\033[0m -  Being happier did not, as many fear, make me a blissed-out zombie. This myth runs deep, all the way back to Aristotle, who said, “All men who have attained excellence in philosophy, in poetry, in art and in politics . . . had a melancholic habitus.” I found that rather than rendering me boringly problem-free, mindfulness made me, as an eminent spiritual teacher once said, “a connoisseur of my neuroses.” One of the most interesting discoveries of this whole journey was that I didn’t need my demons to fuel my drive— and that taming them was a more satisfying exercise than indulging them. Jon Kabat-Zinn has theorized that science may someday show that mindfulness actually makes people more creative, by clearing out the routinized rumination and unhelpful assumptions, making room for new and different thoughts. On retreat, for example, I would be flooded with ideas, filling notebooks with them, scribbling them down on the little sheets of paper between sitting and walking. So, who knows, maybe Van Gogh would have been an even better painter if he hadn’t been so miserable that he sliced off his ear?", "The Way of the Worrier -  commandment six: \033[1m Don’t Force It \033[0m - It’s hard to open a jar when every muscle in your arm is tense. A slight relaxation served me well on the set of GMA, in interpersonal interactions, and when I was writing scripts. I came to see the benefits of purposeful pauses, and the embracing of ambiguity. It didn’t work every time, mind you, but it was better than my old technique of bulldozing my way to an answer.", "The Way of the Worrier -  commandment seven: \033[1m Humility Prevents Humiliation \033[0m - We’re all the stars of our own movies, but cutting back on the number of Do you know who I am? thoughts made my life infinitely smoother. When you don’t dig in your heels and let your ego get into entrenched positions from which you mount vigorous, often irrational defenses, you can navigate tricky situations in a much more agile way. For me humility was a relief, the opposite of humiliation. It sanded the edges off of the comparing mind. Of course, striking the right balance is delicate; it is possible to take this too far and become a pushover. (See precept number two, regarding hiding the Zen.)", "The Way of the Worrier -  commandment eight: \033[1m Go Easy with the Internal Cattle Prod \033[0m - As part of my “price of security” mind-set, I had long assumed that the only route to success was harsh self-criticism. However, research shows that “firm but kind” is the smarter play. People trained in self-compassion meditation are more likely to quit smoking and stick to a diet. They are better able to bounce back from missteps. All successful people fail. If you can create an inner environment where your mistakes are forgiven and flaws are candidly confronted, your resilience expands exponentially.", "The Way of the Worrier -  commandment nine: \033[1m Nonattachment to Results \033[0m - Nonattachment to results + self compassion = a supple relentlessness that is hard to match. Push hard, play to win, but don’t assume the fetal position if things don’t go your way. This, I came to believe, is what T. S. Eliot meant when he talked about learning \"to care and not to care.\"", "The Way of the Worrier -  commandment ten: \033[1m What Matters Most? \033[0m - When worrying about the future, I learned to ask myself: What do I really want? While I still loved the idea of success, I realized there was only so much suffering I was willing to endure. What I really wanted was aptly summed up during an interview I once did with Robert Schneider, the self-described “spastic” lead singer for the psych-pop group, Apples in Stereo. He was one of the happiest-seeming people I’d ever met: constantly chatting, perpetually in motion— he just radiated curiosity and enthusiasm. Toward the end of our interview, he said, \"The most important thing to me is probably, like, being kind and also trying to do something awesome.\""]

listofdicts = [{'author': 'Edwin Catmull', 'quotes': edquotes}, {'author': 'Dale Carnegie', 'quotes': carnegiequotes}, {'author': 'Steve Jobs', 'quotes': stevequotes}, {'author': 'Dan Harris: 10% Happier', 'quotes': danquotes}]


def main():
    parser = optparse.OptionParser()
    parser.add_option("-e", "--edd",
        action="store_true", #tells optparse to store true or None in variable with the same name as option
        help = "The person")

    parser.add_option("-c", "--carnegie",
        action="store_true", #tells optparse to store true or None in variable with the same name as option
        help = "The person")

    parser.add_option("-s", "--steve",
        action="store_true", #tells optparse to store true or None in variable with the same name as option
        help = "The person")

    (options, args) = parser.parse_args()

    if options.edd != None:
        print_random_quote_from_author("Edwin Catmull")
    elif options.carnegie != None:
        print_random_quote_from_author("Dale Carnegie")
    elif options.steve != None:
        print_random_quote_from_author("Steve Jobs")
    else:
        #dict = choose_author()
        #quote = get_random_item_from_list(dict['quotes'])
        #print_quote_and_author(quote, dict['author'])
        #dict = get_random_item_from_list(listofdicts)
        dict = get_weighted_random_item_from_list(listofdicts)
        print_quote_from_dict(dict)

def print_random_quote_from_author(author):
    dict = get_dict_from_author(author)
    print_quote_from_dict(dict)

def print_quote_from_dict(dict):
    quotes = dict['quotes']
    quote = get_random_item_from_list(quotes)
    author = dict['author']
    print_quote_and_author(quote, author)


def get_dict_from_author(author):
    for dict in listofdicts:
        if dict['author'] == author:
            return dict

def choose_author():
    i = random.randint(0,len(listofdicts) - 1)
    return listofdicts[i]


def print_quote_and_author(quote, author):
    print(quote, " - ", author)


'''
Chooses a dictionary from the list according weighted according to the number of quotes,
the more quotes the author have the higher chance the author has of being picked.
Would prabably be easier just to join all the dicts so you just have a list with author and quotes and get_weighted_random_item_from_list
choose one completely at random from the list. But this was more fun to program
'''
def get_weighted_random_item_from_list(list):
    sum = 0 # this will be used for the running sum of the items in the dicts
    i = 0
    weights = []
    for dict in list:
        lenght = len(dict['quotes'])
        sum = sum + lenght
        weights.append({'i': i, 'sum': sum}) # Add the running sum as this weight
        i += 1
    rand = random.randint(1,sum) # Find a random number between one and the total number of quotes in all dicts
    for j in weights:
        if rand <= j['sum']: # For each dict find the one that has a running sum higher than  the random number. But which predecesor had a running sum lower than the random number
            return list[j['i']]
    #return list[i]


def get_random_item_from_list(list):
    i = random.randint(0,len(list) - 1)
    return list[i]


if __name__=='__main__':
    main()
