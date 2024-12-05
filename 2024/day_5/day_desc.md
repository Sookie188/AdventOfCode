# --- Day 5: Print Queue ---

Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning thestationerystacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating avery familiar printerbeckons you over.

The Elf must recognize you, because they waste no time explaining that the newsleigh launch safety manualupdates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in avery specific order. The notationX|Ymeans that if both page numberXand page numberYare to be produced as part of an update, page numberXmustbe printed at some point before page numberY.

The Elf has for you both thepage ordering rulesand thepages to produce in each update(your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:

```shell
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```
The first section specifies thepage ordering rules, one per line. The first rule,47|53, means that if an update includes both page number 47 and page number 53, then page number 47mustbe printed at some point before page number 53. (47 doesn't necessarily need to beimmediatelybefore 53; other pages are allowed to be between them.)

The second section specifies the page numbers of eachupdate. Because most safety manuals are different, the pages needed in the updates are different too. The first update,75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifyingwhich updates are already in the right order.

In the above example, the first update (75,47,61,53,29) is in the right order:

Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.

The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.

The fourth update,75,97,47,61,53, isnotin the correct order: it would print 75 before 97, which violates the rule97|75.

The fifth update,61,13,29, is alsonotin the correct order, since it breaks the rule29|13.

The last update,97,13,75,29,47, isnotin the correct order due to breaking several rules.

For some reason, the Elves also need to know themiddle page numberof each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

```shell
75,47,61,53,29
97,61,53,29,13
75,29,13
```
These have middle page numbers of61,53, and29respectively. Adding these page numbers together gives143.

Of course, you'll need to be careful: the actual list ofpage ordering rulesis bigger and more complicated than the above example.

Determine which updates are already in the correct order.What do you get if you add up the middle page number from those correctly-ordered updates?

