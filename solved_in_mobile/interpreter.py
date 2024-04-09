def interpret(value,command,args):
	prec ={'+':1,'-':1,'*':2}
	evalu={'+': lambda x,y:x+y,
	'-':lambda x,y:x-y,
	'*':lambda x,y:x*y,
	'/':lambda x,y:x/y}
		
	if len(command)>1:
		def interpret1(value,command,args):
			if prec[command[1]]>prec[command[0]]:
				n = evalu[command[1]](value,args[0])
				args.pop(0)
				command.pop(1)		
			elif prec[command[0]]>prec[command[1]]:
					n = evalu[command[0]](value,args[0])
					args.pop(0)
					command.pop(0)
			elif prec[command[0]]==prec[command[1]]:
				n = evalu[command[0]](value,args[0])
				args.pop(0)
				command.pop(0)
								
			interpret(n,command,args)
								
		interpret1(value,command,args)
							
	else:
			n = evalu[command[0]](value,args[0])
			return n

				
interpret(4,['-','+'],[2,16])