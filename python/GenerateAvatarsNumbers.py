import zipfile
import os
import csv
import random
import py_avataaars as pa

# name of csv file 
filename = "tsamg_numbers_import.csv"
# Example usage
folder_to_zip = 'avatars'  
output_zip = 'avatars_numbers.zip' 


def zip_folder(folder_path, output_zip_path):
    # Create a ZipFile object in write mode
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Create the full file path
                file_path = os.path.join(root, file)
                # Calculate the relative path to maintain folder structure
                relative_path = os.path.relpath(file_path, os.path.dirname(folder_path))
                # Add file to the zip
                zipf.write(file_path, relative_path)
                
# https://github.com/kebu/py-avataaars/blob/master/py_avataaars/__init__.py
# Female
FSkinColorOpts=['BLACK','PALE','LIGHT','BROWN','DARK_BROWN','PALE','LIGHT']      
FHairColorOpts=['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED','SILVER_GRAY']
FFacialHairColorOpts=['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
FTopTypeOpts=['HIJAB','TURBAN','WINTER_HAT1','WINTER_HAT2','WINTER_HAT3','WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB','LONG_HAIR_BUN',
            'LONG_HAIR_CURLY','LONG_HAIR_CURVY','LONG_HAIR_FRIDA','LONG_HAIR_FRO','LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
            'LONG_HAIR_MIA_WALLACE','LONG_HAIR_SHAVED_SIDES','LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2','LONG_HAIR_STRAIGHT_STRAND']
FFacialHairTypeOpts=['DEFAULT','DEFAULT','DEFAULT']
FClotheTypeOpts=['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
FClotheGraphicTypeOpts=['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','SELENA','BEAR','SKULL_OUTLINE','SKULL']
FMouthTypeOpts=['DEFAULT','SERIOUS','SMILE','TWINKLE']
FEyesTypeOpts=['DEFAULT','EYE_ROLL','HAPPY','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
FEyebrowTypeOpts=['DEFAULT','DEFAULT_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
FAccessoriesTypeOpts=['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
FHatColorOpts=['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PINK','RED']
FClotheColorOpts=['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PINK','RED']

# Male
MSkinColorOpts=['BLACK','PALE','LIGHT','BROWN','DARK_BROWN','PALE','LIGHT']      
MHairColorOpts=['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED','SILVER_GRAY']
MFacialHairColorOpts=['BLACK','AUBURN','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','SILVER_GRAY']
MTopTypeOpts=['NO_HAIR','HAT','SHORT_HAIR_DREADS_01',
            'SHORT_HAIR_FRIZZLE','SHORT_HAIR_SHORT_CURLY','SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND',
            'SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES','SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
MFacialHairTypeOpts=['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
MClotheTypeOpts=['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
MClotheGraphicTypeOpts=['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','SELENA','BEAR','SKULL_OUTLINE','SKULL']
MMouthTypeOpts=['DEFAULT','SERIOUS','SMILE','TWINKLE']
MEyesTypeOpts=['DEFAULT','EYE_ROLL','HAPPY','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
MEyebrowTypeOpts=['DEFAULT','DEFAULT_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL',
                'UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
MAccessoriesTypeOpts=['DEFAULT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
MHatColorOpts=['BLACK','GRAY_01','GRAY_02','HEATHER']
MClotheColorOpts=['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER']


if not os.path.isdir('avatars'):
    os.mkdir('avatars')
    
with open(filename,newline='\n',encoding='UTF-8') as csvfile: 
    # creating a csv writer object 
    csvreader = csv.reader(csvfile,delimiter=',') 
    # This skips the first row of the CSV file.
    next(csvreader) 
        
    for row in csvreader:
        if bool(random.getrandbits(1)):
            RSCO = random.choice(FSkinColorOpts)
            RHCO = random.choice(FHairColorOpts)
            RTTO = random.choice(FTopTypeOpts)
            RFHTO = random.choice(FFacialHairTypeOpts)
            RFHCO = random.choice(FFacialHairColorOpts)
            RCTO = random.choice(FClotheTypeOpts)
            RCGTO = random.choice(FClotheGraphicTypeOpts)
            RMTO = random.choice(FMouthTypeOpts)
            RETO = random.choice(FEyesTypeOpts)
            REBTO = random.choice(FEyebrowTypeOpts)
            RATO = random.choice(FAccessoriesTypeOpts)
            RCCO = random.choice(FClotheColorOpts)
            RHTCO = random.choice(FHatColorOpts)
        else:
            RSCO = random.choice(MSkinColorOpts)
            RHCO = random.choice(MHairColorOpts)
            RTTO = random.choice(MTopTypeOpts)
            RFHTO = random.choice(MFacialHairTypeOpts)
            RFHCO = random.choice(MFacialHairColorOpts)
            RCTO = random.choice(MClotheTypeOpts)
            RCGTO = random.choice(MClotheGraphicTypeOpts)
            RMTO = random.choice(MMouthTypeOpts)
            RETO = random.choice(MEyesTypeOpts)
            REBTO = random.choice(MEyebrowTypeOpts)
            RATO = random.choice(MAccessoriesTypeOpts)
            RCCO = random.choice(MClotheColorOpts)
            RHTCO = random.choice(MHatColorOpts)
        
        avatar = pa.PyAvataaar(
        style=pa.AvatarStyle.TRANSPARENT,
        skin_color=getattr(pa.SkinColor,RSCO),
        hair_color=getattr(pa.HairColor,RHCO),
        top_type=getattr(pa.TopType,RTTO),
        facial_hair_type=getattr(pa.FacialHairType,RFHTO),
        facial_hair_color=getattr(pa.HairColor,RFHCO),
        clothe_type=getattr(pa.ClotheType,RCTO),
        clothe_graphic_type=getattr(pa.ClotheGraphicType,RCGTO),
        mouth_type=getattr(pa.MouthType,RMTO),
        eye_type=getattr(pa.EyesType,RETO),
        eyebrow_type=getattr(pa.EyebrowType,REBTO),
        accessories_type=getattr(pa.AccessoriesType,RATO),
        clothe_color=getattr(pa.Color,RCCO),
        hat_color=getattr(pa.Color,RHTCO)
        )
        avatar.render_png_file('avatars/'+row[0]+'.png')


zip_folder(folder_to_zip, output_zip)
# fake.password()
# fake.password()