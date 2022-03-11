precision 
embed
<drac2>
cc    = "Mutagencraft - Consume Mutagen"
if not character().cc_exists(cc):
  character().create_cc(cc,0,2,'long','bubble')
v     = character().cc_exists(cc) and character().get_cc(cc)
c     = combat()
out   = []
argList     = "@@@"
args        = argparse(argList)
if c:
  target      = combat().me.name if combat().me else combat().current.name
else:
  err("You need to join your player into initiative before running this alias")
ignore      = args.last('i')
bolsterType = args.adv(custom = {'adv': 'spell', 'dis': 'bonus'})

cTarget = c.get_combatant(target) if c and target else None

if v or ignore:
  cTarget.add_effect("Precision Mutagen", "-sdis str", desc = "Ygv's weapon attacks score a critical hit on a roll of 19-20.\n - Side effect: Ygv has disadvantage on Strength saving throws.")
  character().mod_cc(cc, -1)
  out.append(f""" -f "{cc} {'(-1)'*(not ignore)}|{character().cc_str(cc)}" """)
elif not (v or ignore):

  if character().cc_exists(cc):
    out.append(f""" -f "No uses remaining!|You must finish a long rest before you can use this ability again." -f "{cc}|{character().cc_str(cc)}" """)
  else:
    out.append(f""" -f "Missing Counter|You appear to be missing the counter named {cc}. Please create it and try again." """)

return ' '.join(out)
</drac2>
-title "Ygv injects his Precision Mutagen!"
-f "Ygv's weapon attacks score a critical hit on a roll of 19-20. 
Side effect: Ygv has disadvantage on Strength saving throws."
-color <color>
-thumb "https://images-ext-1.discordapp.net/external/lE9WkjqgsYqFnlmnIn1X-oji92K7H5x5NXBzJrGLhy8/%3Fwidth%3D150%26height%3D150%26fit%3Dcrop%26quality%3D95%26auto%3Dwebp/https/www.dndbeyond.com/avatars/22129/263/1581111423-43322934.jpeg"