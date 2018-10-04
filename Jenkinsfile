#!/usr/bin/env groovy

pipeline {
    agent any
    
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = "${HOME}/cft-jenkins-sa.json"
        JENKINS_SA_ACCOUNT = "cft-jenkins-sa@sourced-root.iam.gserviceaccount.com"
    }
    stages{
        stage('Checkout DM Repo') {
            steps {
                echo '------------------'
                echo 'Cloning github repo' 
                git branch: 'cloud-foundation', url: 'https://github.com/sourced/deploymentmanager-samples'
            }
        }
        stage('Authenticate with ServiceAccount') {
            steps {
                // echo 'printenv'
                // sh 'printenv'
                echo '------------------'
                echo 'Logging into gcloud with $JENKINS_SA_ACCOUNT'
                sh 'gcloud auth activate-service-account $JENKINS_SA_ACCOUNT --key-file=$HOME/cft-jenkins-sa.json'
            }
        }
        stage('Install CloudFoundation ToolKit') {
            steps {
                echo '------------------'
                echo 'checkout tool branch' 
                sh 'git checkout tool'
                echo '------------------'
                echo 'Install CFT tool (make build, sudo make install)'
                sh 'make build && sudo make install'
                echo '------------------'
                echo 'cft help command'
                sh 'cft -h'
            }
        }
        stage('Test Access') {
            steps {
                echo '-----------------'
                echo 'gcloud projects list'
                sh 'gcloud projects list'
                echo '-----------------'
                echo 'gcloud compute networks list'
                sh 'gcloud compute networks list'
                echo '-----------------'
                echo 'gcloud compute networks create test-jenkins-network --project sourced-dmtemplates-praveenc'
                sh 'gcloud compute networks create test-jenkins-network --project sourced-dmtemplates-praveenc'
                
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