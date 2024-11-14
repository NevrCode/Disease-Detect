class DiseaseFeature :
    feature = []
    featureName = []

    '''
    status_mapping = {
    'Yes': 0,
    'No': 1
    }

    gender_mapping = {
        'Female': 0,
        'Male': 1
    }

    lvl_mapping = {
        'Low': 0,
        'Normal': 1,
        'High': 2 
    }
    AGE 
    fever (no, yes)
    cough (no, yes)
    fatigue (no, yes)
    difficult breath (no, yes)
    gender (female, male)
    blood press (high, low, normal)
    kolestrol(high, low, normal)
    '''
    def __init__(self, symtoms : list): 
        self.featureName = ['demam', 'batuk', 'lemas', 'sulit nafas', 'gender', 'tekanan', 'kolesterol']

        for item in self.featureName:
            if item in symtoms:
                self.feature.append(0)  # Append 0 if item is in the checker list
            else:
                self.feature.append(item)  # Otherwise, append the item itself
        

    def getFeature(self) :
        return self.feature
    

        
            

    
