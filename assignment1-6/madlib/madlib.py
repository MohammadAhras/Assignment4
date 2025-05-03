def mad_libs():
    print("🎉 Let's play Mad Libs! Fill in the blanks with your own words.\n")

    name = input("👤 Give me a name: ")
    place = input("📍 Give me a place: ")
    funny_adj = input("😂 Give me a funny adjective: ")
    random_object = input("🎁 Give me a random object: ")
    animal = input("🐾 Give me an animal: ")
    action_verb = input("🏃‍♂️ Give me an action verb: ")
    funny_exclamation = input("😲 Give me a funny exclamation (like 'Oops!' or 'Yikes!'): ")

    story = f'''
    📖 Once upon a time, there was a person named *{name}* who lived in *{place}*.
    One day, they found a *{funny_adj} {random_object}* 🧸.
    Suddenly, a wild *{animal}* appeared and started to *{action_verb}*! 😱
    "{funny_exclamation.upper()}!" they shouted, and the adventure began...
    '''

    print("\n📝 Here is your Mad Libs Story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()