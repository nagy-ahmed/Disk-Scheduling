def fcfs(requests, start_track):
    total_time = 0
    current_track = start_track
    result = []

    for req in requests:
        result.append(req)
        total_time += abs(req - current_track)
        current_track = req

    return result, total_time

def sstf(requests, start_track):
    total_time = 0
    current_track = start_track
    result = []

    while requests:
        closest_track = min(requests, key=lambda x: abs(x - current_track))
        result.append(closest_track)
        total_time += abs(closest_track - current_track)
        current_track = closest_track
        requests.remove(closest_track)

    return result, total_time
  
def look(requests, start_track,direction): 
      
    seek_count = 0
    distance = 0
    cur_track = 0
    left = [] 
    right = [] 
   
    seek_sequence = [] 

    for i in range(len(requests)): 
        if (requests[i] < start_track): 
            left.append(requests[i]) 
        if (requests[i] > start_track): 
            right.append(requests[i]) 
  

    left.sort() 
    right.sort() 

    run = 2
    while (run): 
        if (direction == "left"): 
            for i in range(len(left) - 1, -1, -1): 
                cur_track = left[i] 
  
                # Appending current track to 
                # seek sequence 
                seek_sequence.append(cur_track) 
  
                # Calculate absolute distance 
                distance = abs(cur_track - start_track) 
  
                # Increase the total count 
                seek_count += distance 
  
                # Accessed track is now the new start_track 
                start_track = cur_track 
  
            # Reversing the direction 
            direction = "right"
              
        elif (direction == "right"): 
            for i in range(len(right)): 
                cur_track = right[i] 
  
                # Appending current track to  
                # seek sequence 
                seek_sequence.append(cur_track) 
  
                # Calculate absolute distance 
                distance = abs(cur_track - start_track) 
                  
                # Increase the total count 
                seek_count += distance 
  
                # Accessed track is now new start_track 
                start_track = cur_track 
  
            # Reversing the direction 
            direction = "left"
              
        run -= 1

    return seek_sequence,seek_count
def scan(requests, start_track, direction="right", total_tracks=1):
        
    seek_count = 0
    distance = 0
    cur_track = 0
    left = [] 
    right = [] 
   
    seek_sequence = [] 
    requests.extend([0,total_tracks-1])
    for i in range(len(requests)): 
        if (requests[i] < start_track): 
            left.append(requests[i]) 
        if (requests[i] > start_track): 
            right.append(requests[i]) 
  

    left.sort() 
    right.sort() 

    run = 2
    while (run): 
        if (direction == "left"): 
            for i in range(len(left) - 1, -1, -1): 
                cur_track = left[i] 
                seek_sequence.append(cur_track) 
                distance = abs(cur_track - start_track) 
                seek_count += distance 
                start_track = cur_track 
  
            # Reversing the direction 
            direction = "right"
              
        elif (direction == "right"): 
            for i in range(len(right)): 
                cur_track = right[i] 
  
                # Appending current track to  
                # seek sequence 
                seek_sequence.append(cur_track) 
  
                # Calculate absolute distance 
                distance = abs(cur_track - start_track) 
                  
                # Increase the total count 
                seek_count += distance 
  
                # Accessed track is now new start_track 
                start_track = cur_track 
  
            # Reversing the direction 
            direction = "left"
              
        run -= 1

    return seek_sequence,seek_count

def c_look(requests, start_track, direction):
       
    seek_count = 0
    distance = 0
    cur_track = 0
    left = [] 
    right = [] 
   
    seek_sequence = [] 

    for i in range(len(requests)): 
        if (requests[i] < start_track): 
            left.append(requests[i]) 
        if (requests[i] > start_track): 
            right.append(requests[i]) 
  

    left.sort() 
    right.sort() 

    if (direction == "left"): 
        for i in range(len(left) - 1, -1, -1): 
            cur_track = left[i] 

            # Appending current track to 
            # seek sequence 
            seek_sequence.append(cur_track) 

            # Calculate absolute distance 
            distance = abs(cur_track - start_track) 

            # Increase the total count 
            seek_count += distance 

            # Accessed track is now the new start_track 
            start_track = cur_track 
        for i in range(len(right) - 1, -1, -1): 
            cur_track=right[i]

            # Appending current track to 
            # seek sequence 
            seek_sequence.append(cur_track) 

            # Calculate absolute distance 
            distance = abs(cur_track - start_track) 

            # Increase the total count 
            seek_count += distance 

            # Accessed track is now the new start_track 
            start_track = cur_track 
        
            
    elif (direction == "right"): 
        for i in range(len(right)): 
            cur_track = right[i] 

            # Appending current track to  
            # seek sequence 
            seek_sequence.append(cur_track) 

            # Calculate absolute distance 
            distance = abs(cur_track - start_track) 
                
            # Increase the total count 
            seek_count += distance 

            # Accessed track is now new start_track 
            start_track = cur_track 
        for i in range(len(left)): 
            cur_track = left[i] 

            # Appending current track to 
            # seek sequence 
            seek_sequence.append(cur_track) 

            # Calculate absolute distance 
            distance = abs(cur_track - start_track) 

            # Increase the total count 
            seek_count += distance 

            # Accessed track is now the new start_track 
            start_track = cur_track 

            

    return seek_sequence,seek_count


def c_scan(requests, start_track, direction="right", total_tracks=1):
        
    seek_count = 0
    distance = 0
    cur_track = 0
    left = [] 
    right = [] 
   
    seek_sequence = [] 
    requests.extend([0,total_tracks-1])

    for i in range(len(requests)): 
        if (requests[i] < start_track): 
            left.append(requests[i]) 
        if (requests[i] > start_track): 
            right.append(requests[i]) 
  

    left.sort() 
    right.sort() 


    if (direction == "left"): 
        for i in range(len(left) - 1, -1, -1): 
            cur_track = left[i] 
            seek_sequence.append(cur_track) 
            distance = abs(cur_track - start_track) 
            seek_count += distance 
            start_track = cur_track 
        for i in range(len(right) - 1, -1, -1): 
            cur_track = right[i] 
            seek_sequence.append(cur_track) 
            distance = abs(cur_track - start_track) 
            seek_count += distance 
            start_track = cur_track 
        
            
    elif (direction == "right"): 
        for i in range(len(right)): 
            cur_track = right[i] 
            seek_sequence.append(cur_track) 
            distance = abs(cur_track - start_track) 
            seek_count += distance 
            start_track = cur_track 
        for i in range(len(left)): 
            cur_track = left[i] 
            seek_sequence.append(cur_track) 
            distance = abs(cur_track - start_track) 
            seek_count += distance 
            start_track = cur_track 

    return seek_sequence,seek_count 

