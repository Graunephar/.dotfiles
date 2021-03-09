#!/usr/bin/env python3
import optparse 
import random

edquotes = ["Give a good idea to a mediocre team, and they will screw it, up. Give a mediocre idea to a great team, and they will either, fix it or come up with something better. If you get the team, right, chances are that they’ll get the ideas right.", "When looking to hire people, give their potential to grow, more weight than their current skill level. What they will be, capable of tomorrow is more important than what they can, do today.", "Always try to hire people who are smarter than you. Always, take a chance on better, even if it seems like a potential, threat.", "If there are people in your organization who feel they are not, free to suggest ideas, you lose. Do not discount ideas from, unexpected sources. Inspiration can, and does, come from, anywhere.", "It isn’t enough merely to be open to ideas from others.", "Engaging the collective brainpower of the people you work, with is an active, ongoing process. As a manager, you must, coax ideas out of your staff and constantly push them to, contribute.", "There are many valid reasons why people aren’t candid with, one another in a work environment. Your job is to search for, those reasons and then address them.", "Likewise, if someone disagrees with you, there is a reason.", "Our first job is to understand the reasoning behind their, conclusions.", "Further, if there is fear in an organization, there is a reason, for it—our job is (a) to find what’s causing it, (b) to, understand it, and (c) to try to root it out.", "There is nothing quite as effective, when it comes to shutting, down alternative viewpoints, as being convinced you are, right", "In general, people are hesitant to say things that might rock, the boat. Braintrust meetings, dailies, postmortems, and, Notes Day are all efforts to reinforce the idea that it is okay, to express yourself. All are mechanisms of self-assessment, that seek to uncover what’s real.", "If there is more truth in the hallways than in meetings, you, have a problem.", "Many managers feel that if they are not notified about, problems before others are or if they are surprised in a, meeting, then that is a sign of disrespect. Get over it.", "Careful “messaging” to downplay problems makes you appear, to be lying, deluded, ignorant, or uncaring. Sharing problems, is an act of inclusion that makes employees feel invested in, the larger enterprise.", "The first conclusions we draw from our successes and failures, are typically wrong. Measuring the outcome without, evaluating the process is deceiving.", "Do not fall for the illusion that by preventing errors, you, won’t have errors to fix. The truth is, the cost of preventing, errors is often far greater than the cost of fixing them.", "Change and uncertainty are part of life. Our job is not to, resist them but to build the capability to recover when, unexpected events occur. If you don’t always try to uncover, what is unseen and understand its nature, you will be ill, prepared to lead.", "Similarly, it is not the manager’s job to prevent risks. It is the, manager’s job to make it safe to take them.", "Failure isn’t a necessary evil. In fact, it isn’t evil at all. It is a, necessary consequence of doing something new.", "Trust doesn’t mean that you trust that someone won’t screw, up—it means you trust them even when they do screw up.", "The people ultimately responsible for implementing a plan, must be empowered to make decisions when things go, wrong, even before getting approval. Finding and fixing, problems is everybody’s job. Anyone should be able to stop, the production line.", "The desire for everything to run smoothly is a false goal—it, leads to measuring people by the mistakes they make rather, than by their ability to solve problems.", "Don’t wait for things to be perfect before you share them with, others. Show early and show often. It’ll be pretty when we, get there, but it won’t be pretty along the way. And that’s as, it should be.", "A company’s communication structure should not mirror its, organizational structure. Everybody should be able to talk to, anybody.", "Be wary of making too many rules. Rules can simplify life for, managers, but they can be demeaning to the 95 percent who, behave well. Don’t create rules to rein in the other 5 percent, —address abuses of common sense individually. This is more, work but ultimately healthier.", "Imposing limits can encourage a creative response. Excellent, work can emerge from uncomfortable or seemingly untenable, circumstances.", "Engaging with exceptionally hard problems forces us to think, differently.", "An organization, as a whole, is more conservative and resistant to change than the individuals who comprise it. Do, not assume that general agreement will lead to change — it, takes substantial energy to move a group, even when all are, on board.", "The healthiest organizations are made up of departments, whose agendas differ but whose goals are interdependent. If, one agenda wins, we all lose.", "Our job as managers in creative environments is to protect, new ideas from those who don’t understand that in order for, greatness to emerge, there must be phases of not-so-greatness. Protect the future, not the past.", "New crises are not always lamentable—they test and, demonstrate a company’s values. The process of problemsolving often bonds people together and keeps the culture in, the present.", "Excellence, quality, and good should be earned words,, attributed by others to us, not proclaimed by us about, ourselves.", "Do not accidentally make stability a goal. Balance is more, important than stability.", "Don’t confuse the process with the goal. Working on our, processes to make them better, easier, and more efficient is, an indispensable activity and something we should, continually work on—but it is not the goal. Making the, product great is the goal."]
carnegiequotes = ["Don't criticize, condemn or complain.", "Give honest, sincere appreciation.", "Arouse in the other person an eager want.", "Become genuinely interested in other people.", "Smile.", "Remember that a person's name is to that person the most important sound in any language.", "Be a good listener.", "Encourage others to talk about themselves.", "Talk in terms of the other person's interest.", "Make the other person feel important - and do so sincerely.", "The only way to get the best of an argument is to avoid it.", "Show respect for the other person's opinions.", "Never say, \"You're wrong.\"" , "If you are wrong, admit it quickly and emphatically.", "Begin in a friendly way.", "Get the other person saying, \"Yes, yes\" immediately.", "Let the other person do a great deal of the talking.", "Let the other person feel that the idea is his or hers.", "Try honestly to see things from the other person's point of view.", "Be sympathetic with the other person's ideas and desires.", "Appeal to the nobler motives.", "Dramatize your ideas.", "Throw down a challenge.", "Begin with praise and honest appreciation.", "Call attention to people's mistakes indirectly.", "Talk about your own mistakes before criticizing the other person.", "Ask questions instead of giving direct orders.", "Let the other person save face.", "Praise the slightest and every improvement. Be \"lavish in your praise.\"" , "Give the other person a fine reputation to live up to.", "Use encouragement. Make the fault seem easy to correct.", "Make the other person happy about doing the thing you suggest."]

listofdicts = [{'author': 'Edwin Catmull', 'quotes': edquotes}, {'author': 'Dale Carnegie', 'quotes': carnegiequotes}]


def main():
    parser = optparse.OptionParser()
    parser.add_option("-e", "--edd", 
        action="store_true", #tells optparse to store true or None in variable with the same name as option
        help = "The person") 

    parser.add_option("-c", "--carnegie", 
        action="store_true", #tells optparse to store true or None in variable with the same name as option
        help = "The person") 

    (options, args) = parser.parse_args()   

    if options.edd != None:   
        print_random_quote_from_author("Edwin Catmull")
    elif options.carnegie != None:
        print_random_quote_from_author("Dale Carnegie")
    else: 
        #dict = choose_author()
        #quote = get_random_item_from_list(dict['quotes'])
        #print_quote_and_author(quote, dict['author'])
        dict = get_random_item_from_list(listofdicts)
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

def get_random_item_from_list(list):
    i = random.randint(0,len(list) - 1)
    return list[i]


if __name__=='__main__':
    main()