#!/usr/bin/env groovy

pipeline {
    agent any
    
    stages{
        stage('Checkout DM Repo') {
            steps {
                echo '------------------'
                echo 'Cloning github repo' 
                git branch: 'cloud-foundation', url: 'https://github.com/sourced/deploymentmanager-samples'
            }
        }
        stage('Test Access') {
            // environment {
            //     CFT_ORGANIZATION_FOLDER_ID = """${sh(
            //             returnStdout: true,
            //             script: 'cp /home/tomcat/cft-env-vars . && . ./cft-env-vars && echo $CFT_ORGANIZATION_FOLDER_ID'
            //         )}""" 
            //     CFT_ORGANIZATION_ID = """${sh(
            //             returnStdout: true,
            //             script: 'cp /home/tomcat/cft-env-vars . && . ./cft-env-vars && echo $CFT_ORGANIZATION_ID'
            //         )}""" 
            //     CFT_BILLING_ACCOUNT_ID = """${sh(
            //             returnStdout: true,
            //             script: 'cp /home/tomcat/cft-env-vars . && . ./cft-env-vars && echo $CFT_BILLING_ACCOUNT_ID'
            //         )}""" 
            //     CFT_PIPELINE_DEPLOYER_ROLE = """${sh(
            //             returnStdout: true,
            //             script: 'cp /home/tomcat/cft-env-vars . && . ./cft-env-vars && echo $CFT_PIPELINE_DEPLOYER_ROLE'
            //         )}""" 
            // }
            steps {
                echo '-----------------'
                echo 'Source CFT_ENV_VARS'
                sh 'source $HOME/cft-env-vars'
                echo '-----------------'
                sh 'printenv'
                echo '-----------------'
                echo 'gcloud projects list'
                sh 'gcloud projects list'
                echo '-----------------'
                echo 'gcloud compute networks list'
                sh 'gcloud compute networks list'
                echo '-----------------'
                echo 'gcloud deployment-manager deployments list'
                sh 'gcloud deployment-manager deployments list'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}