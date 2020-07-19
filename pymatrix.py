# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:54:33 2019

@author: sdevl
"""

def pymatrix (dmx):

#build data matrix

# data matrix has 6 columns
#   col 1 is time
#   col 2 is rat x position
#   col 3 is rat y position
#   col 4 is cluster ids of spike events
#   col 5 is event flag
#   col 6 is visit number


#LOAD DATA
#file path
    filepath = 'C:\Users\sdevl\Desktop\Recording\R2004' #NEEDS FUTURE HELP
    full_filepath = [filepath, '\10-04-18'] #NEEDS FUTURE HELP
    
#load video
    filename_vt = [full_filepath, '\VT1.nvt']
    [TimestampsVT, X, Y] = Nlx2MatVT(filename_vt, [1 1 1 1 1 1], 1, 1, [])
    
#load tt
    filname_tt = [full_filepath, '/TT']
    ttcols = loadtt(filname_tt)
    
#load events
    filname_ev = [full_filepath, '/Events.nev'] 
    [TimeStampsEV, ~, ~, ~, ~, ~] = Nlx2MatEV(filname_ev, [1 1 1 1 1], 1, 1, [])


#DATA PREP AND COMBINE
#video data
    datamtx_vt = [TimestampsVT' X' Y'  nan(size(TimestampsVT',1), 2) ]
    datamtx_vt(X==0 & Y==0, [2 3]) = nan

#tetrode data
    datamtx_tt = [ ttcols(:,1) nan(size(ttcols(:,1),1), 4) ]
    datamtx_tt(:,4) = ttcols(:,2)

#event data
    datamtx_ev = [ TimeStampsEV' nan(size(TimeStampsEV',1), 4) ]
    datamtx_ev(:,5) = 1

#combine matrices
    datamtx = [ datamtx_ev; datamtx_vt; datamtx_tt ]
    datamtx = sortrows(datamtx, 1)

#INTERP POS
#interpX
    times_of_video_xs = datamtx(~isnan(datamtx(:,2)), 1)
    video_xs = datamtx(~isnan(datamtx(:,2)), 2)
    times_of_missing_xs = datamtx(isnan(datamtx(:,2)), 1)
    interped_xs = interp1(times_of_video_xs, ...
    video_xs, times_of_missing_xs, 'linear')
    datamtx(isnan(datamtx(:,2)),2) = interped_xs
    
#interpY
    times_of_video_ys = datamtx(~isnan(datamtx(:,3)), 1)
    video_ys = datamtx(~isnan(datamtx(:,3)), 3)
    times_of_missing_ys = datamtx(isnan(datamtx(:,3)), 1)
    interped_ys = interp1(times_of_video_ys, ...
    video_ys, times_of_missing_ys, 'linear')
    datamtx(isnan(datamtx(:,3)),3) = interped_ys
    
#TIME CORRECTION
    datamtx(:,1) = (datamtx(:,1)- min(datamtx(:,1)))./1000000


#COLUMN 6 VISIT NUMBERS
#add column for visit numbers
#   context visits are labeled 1:4   
#   iti (including pre and post) 5:9
    datamtx(:,6) = nan
    visit_order = [5 1 6 2 7 3 8 4 9]
#visit_order = [6 1 7 2 8 3 9 4 10 5 11]
    vis_counter = 0
#iterate through all the rows
    for itw = 2:size(datamtx,1)-1:
# if flag
        if datamtx(itw,5)==1:
            vis_counter = vis_counter+1
        
#fill in
        datamtx(itw,6) = visit_order[vis_counter]
    datamtx(-1,6) = visit_order[vis_counter]
