pipeline {
    agent any
    
    parameters {
        string(name: 'MY_PARAM', defaultValue: 'Hello xinh cuộc sống đẹp xinh', description: 'Enter a value for MY_PARAM')
      
    }

    environment {
        MY_ENV_VAR = "${params.MY_PARAM}"
        VENV = "/Users/test/Working/Jenkins/workspace/python-jobs/python-pipeline/venv"
        ALLURE_RESULTS_DIR = 'allure-results-001'
        ALLURE_REPORT_DIR = 'allure-report'
    }

    stages {
        
        // stage('Checkout') {
        //     steps {
        //         // Checkout the repository
        //         git credentialsId: credentials('github'), url: 'https://github.com/pvo-cicd/python-tests.git', branch: 'master'
        //     }
        // }
        
        stage('Clean Workspace') {
            steps {
                deleteDir()  // This deletes the entire workspace before each build
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install - requirements.text
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run the tests
                    sh '''
                    source venv/bin/activate
                    cd ~/Working/Jenkins/python-tests/
                    pytest --alluredir=${ALLURE_RESULTS_DIR} *.py
                    '''
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false, 
                        results: [[path: '${ALLURE_RESULTS_DIR}']]  // Path to allure results folder
                    ])
                }
            }
        }
        // stage('Generate Allure Report') {
        //     steps {
        //         sh '''
        //         allure generate ${ALLURE_RESULTS_DIR} -o ${ALLURE_REPORT_DIR} --clean
        //         '''
        //     }
        // }
        // stage('Archive Allure Report') {
        //     steps {
        //         archiveArtifacts artifacts: "${ALLURE_REPORT_DIR}/**", fingerprint: true
        //     }
        // }
        
        stage('Clean Up') {
            steps {
                // Clean up the virtual environment (optional)
                sh 'rm -rf MY_ENV_VAR'
            }
        }
    }
    // post {
    //     always {
    //         // Publish Allure report
    //         allure([
    //             includeProperties: false, 
    //             results: [[path: 'allure-results']]
    //         ])
    //     }
    // }
     post {
        // always {
        //     // sh 'chmod -R 777 allure-results'
        //     allure([
        //         includeProperties: false,
        //         results: [[path: '${ALLURE_RESULTS_DIR}']]
        //     ])
        // }
        cleanup {
            cleanWs() // Clean the workspace after the build
        }
    }
}
        // stage('Checkout') {
        //     steps {
        //         // Checkout the repository
        //         git 'https://github.com/your-username/my-python-project.git'
        //     }
        // }
        // stage('Set Up Python Environment') {
        //     steps {
        //         script {
        //             // // Check if virtualenv is installed
        //             // sh '''
        //             // if ! command -v python3 &> /dev/null; then
        //             //     echo "Python 3 is not installed!"
        //             //     exit 1
        //             // fi
        //             // # Create a virtual environment if it doesn't exist
        //             // if [ ! -d "$VENV_DIR" ]; then
        //             //     python3 -m venv $VENV
        //             // fi
        //             // '''
                    
        //             // Create virtual environment (optional but recommended)
        //             // sh 'python3 -m venv $VENV'
        //             // Activate the virtual environment
        //             // sh 'python3 -m venv $VENV'
        //             // sh 'source $VENV/bin/activate'
        //             // sh 'pip install --upgrade pip'
        //             // // Install dependencies (if you have a requirements.txt)
        //             // sh 'pip install allure-pytest'
        //         }
        //     }
        // }
        // stage('Generate Allure Report') {
        //     steps {
        //         sh '''
        //         allure generate ${ALLURE_RESULTS_DIR} -o ${ALLURE_REPORT_DIR} --clean
        //         '''
        //     }
        // }
        // stage('Archive Allure Report') {
        //     steps {
        //         archiveArtifacts artifacts: "${ALLURE_REPORT_DIR}/**", fingerprint: true
        //     }
        // }
        // stage('Generate Allure Report') {
        //     steps {
        //         script {
        //             allure([
        //                 includeProperties: false, 
        //                 jdk: '', 
        //                 results: [[path: "${ALLURE_RESULTS_DIR}"]]
        //             ])  // Generate the Allure report from the results
        //         }
        //     }
        // }
        // stage('Publish Allure Report') {
        //     steps {
        //         allure([
        //             includeProperties: false, 
        //             jdk: '', 
        //             results: [[path: "${ALLURE_RESULTS_DIR}"]]
        //         ])  // Publish Allure report to Jenkins
        //     }
        // }
        
        
        
        
    
    

