def fibolist(mijn_lijst, max_legte):
    if len(mijn_lijst) == max_legte:
        return mijn_lijst
    else:
        mijn_lijst.append(mijn_lijst[-1] +  mijn_lijst[-2])
        # laatse en voorlaatse element optelen en aan de lijst toevoegen
        return (fibolist(mijn_lijst, max_legte))
print(fibolist([0, 1],50))