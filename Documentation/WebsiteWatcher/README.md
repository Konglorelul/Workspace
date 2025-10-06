## Alarm Workflow Review 

### 1. Overview  

“This workflow builds and tests the alarm package created in the repo”

---

### 2. Problem / Why Changes Were Needed  

“Build was failing because the workflow file was written poorly, the package was installed from an outdated version repository.”

---

### 3. What I Changed  
List the key edits you made.

- Changed the package installation from pypi repo to our repo
- Adjusted dependecies install commands from 2 separate commands into one pip install -r requirements.txt
- Added trigger on testing-branch action
- Organized code to have a follow up logic

---

### 4. How It Works Now  
 
“The workflow triggers on pull requests on the testing-branch. It sets the environment, upgrades pip, relocates to the package directory and installs the package, installs package dependencies and runs tests”

---

### 5. Issues Encountered & Fixes  

- YAML command issue → Can't install package from repo in 2 concurrent commands, multiline must be used. First cd to the package directory then install the package from said directory

---

### 6. Assumptions / Requirements  

- Requires requirements.txt 

---

### 7. Next Steps / Improvements (Optional)  

---

### 8. Files Affected  
 
`.github/workflows/testpack.yml`
