import json, argparse
from word_db import Word_DB


# input file processing
def process_words(word_db, in_file, out_file):
    with open(in_file) as i:
        with open(out_file, "w", encoding="UTF-8") as o:
            dismissed_words = []
            comment_block = False
            for w in i.readlines():
                w = w.strip()
                
                if comment_block: # currently in a comment block
                    if w[:2] != ")#": continue # comment block did not end here
                    comment_block = False
                    w = w[2:].strip() # comment block did end - parse the rest of the current line as normal

                if len(w) == 0: continue

                if w[0] == "_": 
                    dismissed_words.append(w[1:].strip()) # dismissed word
                    continue
                
                if w[0] == "#": # start of comment
                    if len(w) == 1: continue
                    if w[1] == "(": # start comment block
                        comment_block = True
                    elif w[1] == "#": # is not a hidden comment
                        o.write(w+"\n\n") 
                    continue # ignore the rest of this line

                else: # regular word
                    print_word(o, word_db, w)
                    
            if len(dismissed_words) != 0: o.write("\n {} \n\n".format("#"*10 + " DISMISSED WORDS " + "#"*10))
            for w in dismissed_words:
                print_word(o, word_db, w)


# output formatting
def print_word(o_stream, word_db, word):
    data = word_db.get(word)
    for r in data.get("results", []):
        s = r["id"].capitalize() + "\n"
        s += "https://www.lexico.com/{}/definition/{}\n".format(word_db.c.language, r["id"])
        for le in r["lexicalEntries"]:
            s += "{}: {}\n".format(
                le.get("lexicalCategory", {}).get("text", ""),
                ", ".join([
                    "{}".format(
                        p.get("phoneticSpelling", ""),
                        ", ".join(p.get("dialects", [])) # dialects currently not shown, see format string above
                    ) for p in le.get("pronunciations", [])
                ])
            )
            
            for entry in le["entries"]:
                for sense in entry["senses"]:
                    for d in sense.get("definitions", []):
                        s += "\tDEF: {}\n".format(d)
                    for e in sense.get("examples", []):
                        s += "\t\t\t{}\n".format(e["text"].capitalize())
                    for subsense in sense.get("subsenses", []):
                        for d in subsense.get("definitions", []):
                            s += "\t\tDEF: {}\n".format(d)
                        for e in subsense.get("examples", []):
                            s += "\t\t\t\t{}\n".format(e["text"].capitalize())

            
            etym_s = ""
            for entry in le["entries"]:
                for etym in entry.get("etymologies", []):
                    etym_s += "\t\t{}\n".format(etym)
            if etym_s != "":
                s += "\n\tEtymologies:\n{}\n".format(etym_s)
            else: s += "\n"
                
        s += "\n"

        o_stream.write(s)

    
def create_argument_parser():
    p = argparse.ArgumentParser(description="Fetch and format word definitions")
    p.add_argument("-i",    dest="input_path",  default="in_words.txt",     help="Input word file")
    p.add_argument("-o",    dest="output_path", default="out_words.txt",    help="Formatted output file")
    p.add_argument("--db",  dest="db_path",     default=".words.db",        help="Word database file (only used if caching is enabled in config)")
    return p
    
    
def main():
    args = create_argument_parser().parse_args()
    
    db = Word_DB(args.db_path)
    process_words(db, args.input_path, args.output_path)

    if db.changed: db.save()
    



main()
