pipeline {
    agent any
    
    parameters {
        string(name: 'MY_PARAM', defaultValue: 'Hello xinh cuộc sống đẹp xinh', description: 'Enter a value for MY_PARAM')
        string(name: 'BRANCH', defaultValue: 'master', description: 'Enter a value for MY_PARAM')
      
    }

    environment {
        MY_ENV_VAR = "${params.BRANCH}"
        VENV = "/Users/test/Working/Jenkins/workspace/python-jobs/python-pipeline/venv"
        ALLURE_RESULTS_DIR = 'allure-results-001'
        ALLURE_REPORT_DIR = 'allure-report'
    }

    options {
            // Keep the last 5 builds and delete older builds
            buildDiscarder(logRotator(numToKeepStr: '5'))
        }

    stages {
        
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run the tests
                    sh '''
                    source venv/bin/activate
                    cd my-python-tests
                    pytest --alluredir=${ALLURE_RESULTS_DIR} *.py
                    '''
                }
            }
        }

        stage('Archive Allure Report') {
            steps {
                archiveArtifacts artifacts: "${ALLURE_REPORT_DIR}/**", fingerprint: true
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
        //     allure([
        //         includeProperties: false,
        //         results: [[path: '${ALLURE_RESULTS_DIR}']]
        //     ])
        // }
        cleanup {
            steps {
                // Clean up the virtual environment (optional)
                sh 'rm -rf MY_ENV_VAR'
            }
            cleanWs() // Clean the workspace after the build
        }
    }
}