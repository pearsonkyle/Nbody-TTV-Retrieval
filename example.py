from nbody.simulation import generate, analyze, report
from nbody.tools import mjup,msun,mearth

if __name__ == "__main__":
    
    # units: Msun, Days, au
    objects = [
        {'m':1.},
        {'m':22*mearth/msun, 'P':0.792, 'inc':3.14159/2, 'e':0, 'omega':0 }, 
        {'m':73.4*mearth/msun, 'P':1.65, 'inc':3.14159/2, 'e':0.029,  'omega':1.92  }, 
        #{'m':0.432*mjup/msun, 'P':12, 'inc':3.14159/2, 'e':0,  'omega':0  }, 
    ]

    # create REBOUND simulation
    sim_data = generate(objects, objects[1]['P']*30, int(30*objects[1]['P']*24) )

    # collect the analytics of interest from the simulation
    ttv_data = analyze(sim_data)

    # plot the results 
    report(ttv_data)
    
    dude()
    #, savefile='report.png')
    
    import numpy as np
    ttv = ttv_data['planets'][0]['ttv']
    epochs = np.arange(len(ttv))
    ttdata = ttv_data['planets'][0]['tt'] + np.random.normal(0,0.5,len(ttv))/(24*60)
    err = (30+np.random.normal(30,30,len(ttv))) /(24*60*60)
    np.vstack([epochs, ttdata, err]).T
    np.savetxt('sim_data.txt',np.vstack([epochs, ttdata, err]).T, header="{}".format(objects))